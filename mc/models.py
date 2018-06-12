from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
# Create your models here.

class Album(models.Model):
    artist = models.ForeignKey(models.Artist)
    #user = models.ForeignKey(User, default=1)
    publisher = models.CharField(max_length=100)
    release_date = models.DateField(default=datetime(1970, 1, 1))


class Artist(models.Model):
    name = models.CharField(max_length = 100)
    sex = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    is_group = models.BooleanField()


class Track(models.Model):
    filename = models.CharField(max_length=100)
    artist = models.ForeignKey(models.Artis)
    album = models.ForeignKey(models.Album)
    is_lyrics_available = models.BooleanField()
    lyrics = models.TextField(max_length=500)