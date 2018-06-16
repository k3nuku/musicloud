from django.shortcuts import render, redirect
from django.http import HttpResponse
from mc.forms import RegistrationForm, TrackForm, SearchForm, UploadForm
from django.contrib.auth.decorators import login_required
from mc.models import Track, Artist, Album
from mc.apps import parse_id3, convert_date, get_albumart, get_media
from django.core.files.base import ContentFile
import hashlib


def index(request, index_type=''):
    if index_type == 'artists':
        artists = Artist.objects.all()

        return render(request, 'index_artist.html',
                      {
                          'artists': artists,
                          'is_main_page': (index_type == 'main') and True or False
                      })
        pass
    elif index_type == 'albums':
        albums = Album.objects.all()

        return render(request, 'index_album.html',
                      {
                          'albums': albums,
                          'is_main_page': (index_type == 'main') and True or False
                      })
        pass
    else:
        songs = Track.objects.all()

        return render(request, 'index.html',
                      {
                          'songs': songs,
                          'is_main_page': (index_type == 'main') and True or False
                      })


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return HttpResponse('form is not valid')

    return render(request, 'register.html', {'form': RegistrationForm})


def search(request):
    form = SearchForm(request.GET)

    if form.is_valid():
        search_string = form.cleaned_data['query']

    pass


@login_required
def profile(request):
    pass


@login_required
def favorites(request):
    pass


@login_required
def upload_track(request):
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES)

        id3 = parse_id3(request.FILES['media'].temporary_file_path())

        album = id3['album'][0]
        artist = id3['artist'][0]
        title = id3['title'][0]
        genre = id3['genre'][0]
        release_date = id3['date'][0]

        artist_check = Artist.objects.filter(name=artist)

        if not artist_check.exists():
            artist_obj = Artist()
            artist_obj.name = artist
            artist_obj.is_group = False
            artist_obj.save()
        else:
            artist_obj = artist_check[0]

        album_check = Album.objects.filter(name=album)

        if not album_check.exists():
            album_obj = Album()
            album_obj.name = album
            album_obj.artist = artist_obj
            album_obj.release_date = convert_date(release_date)
            #album_obj.image = ContentFile(
            #    get_albumart(request.FILES['media'].temporary_file_path()))
            album_obj.publisher = ''
            album_obj.save()
        else:
            album_obj = album_check[0]

        if form.is_valid():
            if not Track.objects.filter(name=title).exists():
                obj = form.save()

                obj.name = title
                obj.artist = artist_obj
                obj.album = album_obj
                obj.save()

            return redirect('index')

    return render(request, 'upload.html', {'form': TrackForm})


@login_required
def download_track(request):
    pass


@login_required
def streaming_track(request):
    pass
