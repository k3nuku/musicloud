from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from mc.models import Album, Track, Artist


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'is_group']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'artist', 'publisher', 'release_date']


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['name', 'artist', 'album', 'filename', 'is_lyrics_available', 'lyrics']

    file = forms.FileField()


class SearchForm(forms.Form):
    query = forms.CharField(required=True)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nickname = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
