from django.conf.urls import patterns, url
from .views import ComentarioCreateView

urlpatterns = patterns('',
    url(r'^/(?P<slug>[\w-]+)$', ComentarioCreateView.as_view(), name='comentario.views.createview'),
    )