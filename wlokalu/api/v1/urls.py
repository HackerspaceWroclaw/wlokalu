#!/usr/bin/python

from django.conf.urls.defaults import *
from django.conf import settings

#-----------------------------------------------------------------------------

urlpatterns = patterns('wlokalu.api.v1.views',
  (r'^$', 'list_elements', {'subpages': ['person', 'sensor']}),
  (r'^person/?$', 'list_presence'),
  (r'^person/(?P<nick>.+)$', 'person'),
  (r'^sensor/?$', 'list_sensors'),
  (r'^sensor/(?P<sensor_id>[^/]+)/?$', 'sensor'),
  (r'^sensor/(?P<sensor_id>[^/]+)/(?P<sensor_subid>.+)$', 'list_complex_sensor'),
)

#-----------------------------------------------------------------------------
# vim:ft=python:nowrap:foldmethod=marker
