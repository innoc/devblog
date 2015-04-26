from django.conf.urls import patterns, include, url
from django.contrib import admin
import logging

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('devblog.urls')),
)