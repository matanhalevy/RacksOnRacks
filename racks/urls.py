__author__ = 'Jason'
import os
from django.conf.urls import patterns, url
from racks import views
from django.conf import settings # New Import
from django.conf.urls.static import static # New Import


urlpatterns = patterns('',
    url(r'$^', views.home, name="RacksOnRacks"),
    url(r'^map/$', views.map, name='map'),
    url(r'^map_locations/$', views.map_locs, name='maplocations'),
    url(r'^fave/$', views.add_favorite,name='fave'),
    url(r'^user_list/$', views.get_users,name='userlist'),
    url(r'^fave_list/$', views.get_faves, name='favelist'),
    url(r'^used/$', views.add_used, name='usedlist'),
    url(r'^about/$', views.about, name='About Page')
    )  # New!

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

