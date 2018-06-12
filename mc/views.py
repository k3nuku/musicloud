from django.shortcuts import render, redirect
from django.http import HttpResponse
from mc.forms import RegistrationForm, TrackForm, SearchForm
from django.contrib.auth.decorators import login_required
from mc.models import Track


def index(request, index_type=''):
    if index_type == 'artists':
        pass
    elif index_type == 'albums':
        pass
    else:
        songs = Track.objects.all()

        return render(request, 'index.html', {'songs': songs})


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

        if form.is_valid():
            pass

    return render(request, 'upload.html', {'form': TrackForm})


@login_required
def download_track(request):
    pass


@login_required
def streaming_track(request):
    pass
