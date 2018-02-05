from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^destination/(?P<pk>[0-9]+)/$', views.destination, name='destination'),
]