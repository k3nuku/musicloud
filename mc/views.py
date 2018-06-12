from django.shortcuts import render, redirect
from django.http import HttpResponse
from mc.forms import RegistrationForm


def index(request):
    return render(request, 'index.html')


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
    pass


def upload_track(request):
    pass


def download_track(request):
    pass


def streaming_track(request):
    pass
