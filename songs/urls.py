from django.conf.urls import url

from . import views

app_name = 'songs'

urlpatterns = [
    url(r'performer/(?P<pk>\d+)/$', views.performer_detail, name='performer'),
    url(r'song/(?P<pk>\d+)/$', views.song_detail, name='detail'),
    url(r'', views.song_list, name='list'),
]
