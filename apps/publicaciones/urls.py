from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('',
    url(r'^/$', PublicacionListView.as_view(), name='publicaciones.views.listview'),
    url(r'^/(?P<nombre>[-_\w]+)/$', CategoriaListView.as_view(), name='categorias.views.listview'),
    url(r'^/(?P<slug>[\w-]+)$', PublicacionDetailView.as_view(), name='publicaciones.views.detailview'),
    )