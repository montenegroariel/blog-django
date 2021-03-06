"""eatnea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from eatnea.views import home, nosotros, quienessomos, equipo, logros, formaparte, acercaeat, cienciatecnologia, cooperacioninternacional, desarrollolocal, empresasemprendimientos, quehacemos


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^acerca-eat', acercaeat, name='acerca-eat'),
    url(r'^nosotros', nosotros, name='nosotros'),
    url(r'^quienes-somos', quienessomos, name='quienes-somos'),
    url(r'^equipo', equipo, name='equipo'),
    url(r'^logros', logros, name='logros'),
    url(r'^forma-parte', formaparte, name='forma-parte'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/filebrowser/', include('filebrowser.urls')),
    url(r'^publicaciones', include('apps.publicaciones.urls', namespace='publicaciones')),
    # Menu Areas
    url(r'^que-hacemos', quehacemos, name='que-hacemos'),
    url(r'^ciencia-tecnologia', cienciatecnologia, name='ciencia-tecnologia'),
    url(r'^cooperacion-internacional', cooperacioninternacional, name='cooperacion-internacional'),
    url(r'^desarrollo-local', desarrollolocal, name='desarrollo-local'),
    url(r'^empresas-emprendimientos', empresasemprendimientos, name='empresas-emprendimientos'),
    # Server static files
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, }),
    #url(r'^ckeditor/', include('ckeditor.urls')),

]

if settings.DEBUG == True:
    urlpatterns += staticfiles_urlpatterns()
