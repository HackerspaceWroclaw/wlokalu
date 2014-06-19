#!/usr/bin/python

from django.conf.urls.defaults import *
from django.conf import settings

#-----------------------------------------------------------------------------

urlpatterns = patterns('wlokalu.views',
  (r'^$', 'list'),
  (r'^nick/(?P<nick>[^/]+)$', 'list'),
  (r'^api/v1/', include('wlokalu.api.v1.urls')),
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
