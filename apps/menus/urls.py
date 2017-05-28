from django.conf.urls import patterns, url
from .views import NosotrosTemplateView


urlpatterns = patterns('',
    url(r'^/nosotros$', NosotrosTemplateView.as_view(), name='template.view.nosotros'),
    )