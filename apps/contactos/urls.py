from django.conf.urls import patterns, url
from .views import ContactoView, ContactoTemplateView

urlpatterns = patterns('',
    url(r'^/$', ContactoView.as_view(), name='contacto.form'),
    url(r'^/gracias/$', ContactoTemplateView.as_view(), name='contacto.views.form'),
    )