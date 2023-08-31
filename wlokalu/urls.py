#!/usr/bin/python

from django.conf.urls import re_path, include
from django.conf import settings
from wlokalu.views import list

#-----------------------------------------------------------------------------

urlpatterns = [
  re_path(r'^$', list, name='list'),
  re_path(r'^nick/(?P<nick>[^/]+)$', list, name='list'),
  re_path(r'^api/v1/', include('wlokalu.api.v1.urls')),
  re_path(r'^static/(?P<path>.+)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }, name = "static_files"),
]

if settings.WLOKALU_USE_ADMIN_IFACE:
  from django.contrib import admin
  urlpatterns += [ re_path(r'^admin/', include(admin.site.urls)) ]

#-----------------------------------------------------------------------------
# vim:ft=python:nowrap:foldmethod=marker
