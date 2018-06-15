from django.db import models
from datetime import datetime


class Artist(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/artist', blank=True)
    is_group = models.BooleanField()

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/album', blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    publisher = models.CharField(max_length=100)
    release_date = models.DateField(default=datetime(1970, 1, 1))

    def __str__(self):
        return self.name + '(' + self.artist.name + ')'


class Track(models.Model):
    name = models.CharField(max_length=250)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    media = models.FileField(upload_to='tracks', null=True)
    is_lyrics_available = models.BooleanField()
    lyrics = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.artist.name + '-' + self.name
