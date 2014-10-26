from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from .contentProvider.views import *

urlpatterns = patterns('',
    url(r'^upload/', csrf_exempt(UploadView.as_view())),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^videos/(?P<tag>[a-zA-Z0-9]+)/$', tagged_videos),
    url(r'videos/?P<video_id>[0-9]+/$', get_video),
)
