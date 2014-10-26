from django.conf.urls import patterns, include, url
from django.contrib import admin
from contentProvider import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^videos/(?P<tag>[a-zA-Z0-9]+)/$', views.tagged_videos),
    url(r'videos/?P<video_id>[0-9]+/$', views.get_video)
)
