#!/usr/bin/python

from django.conf.urls.defaults import *
from django.conf import settings

#-----------------------------------------------------------------------------

urlpatterns = patterns('wlokalu.views',
  (r'^hello/?$', 'hello_world'),
  (r'^$', 'list'),
)

#-----------------------------------------------------------------------------

urlpatterns += patterns('',
  url(
    r'^static/(?P<path>.+)$',
    'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT },
    name = "static_files"
  ),
)

if settings.WLOKALU_USE_ADMIN_IFACE:
  from django.contrib import admin
  urlpatterns += patterns('', (r'^admin/', include(admin.site.urls)))

#-----------------------------------------------------------------------------
# vim:ft=python:nowrap:foldmethod=marker
