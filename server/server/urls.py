from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from .contentProvider.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^upload/', csrf_exempt(UploadView.as_view())),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^videos/(?P<tag>[a-zA-Z]+)/$', tagged_videos),
    url(r'^videos/(?P<video_id>[0-9]+)/$', get_video),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
