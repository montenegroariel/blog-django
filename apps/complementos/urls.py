from django.conf.urls import patterns, url
from .views import ciudades_ajax


urlpatterns = patterns('',
    url(r'^/ajax/ciudades/$', ciudades_ajax, name='ciudades'),
    )