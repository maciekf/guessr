from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from .contentProvider.views import *

urlpatterns = patterns('',
    url(r'^$', csrf_exempt(UploadView.as_view())),
    url(r'^admin/', include(admin.site.urls)),
)
