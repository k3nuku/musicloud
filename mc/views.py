from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from musicloud.forms import AlbumForm, TrackForm, UserForm
from mc.models import Album, Track, Artist


# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # login success
                return render(request, 'template/index.html', {})
            return  # account is not active
        else:
            return  # login fail


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'template/index.html')


def index(request):
    return render(request, 'template/index.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'template/index.html', )
            else:
                return render(request, '')

    pass


def search(request):
    pass


def upload_track(request):
    pass


def download_track(request):
    pass


def streaming_track(request):
    pass
