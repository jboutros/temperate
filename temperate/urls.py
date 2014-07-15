from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^private/admin/', include(admin.site.urls)),
    url(r'^', include('nestcontrol.urls')),
    url(r'^', include('django.contrib.auth.urls')),
)
