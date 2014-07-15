from django.conf.urls import patterns, url
from .views import app_home

urlpatterns = patterns('',
    url(r'^$', app_home, name='app_home'),
)
