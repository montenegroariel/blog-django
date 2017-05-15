from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from eatnea.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/filebrowser/', include('filebrowser.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG == True:
    urlpatterns += staticfiles_urlpatterns()


