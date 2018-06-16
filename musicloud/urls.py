"""musicloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from mc import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, {'index_type': 'main'}, name='index'),
    url(r'^songs/$', views.index, {'index_type': 'songs'}, name='index_songs'),
    url(r'^artists/$', views.index, {'index_type': 'artists'}, name='index_artists'),
    url(r'^albums/$', views.index, {'index_type': 'albums'}, name='index_albums'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^upload/$', views.upload_track, name='upload_track'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^favorites/$', views.favorites, name='favorites'),
    path('search/', views.search, name='search'),
    url(r'^download/([0-9]+)', views.download_track, name='download_track'),
    url(r'^streaming/([0-9]+)', views.streaming_track, name='streaming_track'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
