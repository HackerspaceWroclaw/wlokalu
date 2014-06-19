#!/usr/bin/python

from django.conf.urls.defaults import *
from django.conf import settings

#-----------------------------------------------------------------------------

urlpatterns = patterns('wlokalu.api.v1.views',
  (r'^person/(?P<nick>.+)$', 'person'),
  (r'^sensor/(?P<sensor_id>[^/]+)$', 'sensor'),
)

#-----------------------------------------------------------------------------
# vim:ft=python:nowrap:foldmethod=marker
