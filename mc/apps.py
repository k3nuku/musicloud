from io import StringIO
from tempfile import TemporaryFile
from django.apps import AppConfig
from mutagen.easyid3 import EasyID3
from datetime import datetime
from PIL import Image

class McConfig(AppConfig):
    name = 'mc'


def parse_id3(file):
    id3 = EasyID3(file)

    return {'title': id3['title'], 'album': id3['album'],
            'artist': id3['artist'], 'genre': id3['genre'],
            'date': id3['date']}


def get_albumart(file):
    id3 = EasyID3(file)

    with TemporaryFile() as f :
        f.write(id3.get('APIC')[0].data)
        f.seek(0)
        data = f.read()

    return data


def convert_date(yyyymmdd):
    datetime_obj = datetime.strptime(yyyymmdd, '%Y%m%d')

    return datetime_obj.strftime('%Y-%m-%d')


def get_PIL_data(image):
    return Image.open(image)