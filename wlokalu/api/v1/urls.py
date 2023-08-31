#!/usr/bin/python

from django.conf.urls import patterns, url, include
from django.conf import settings

from wlokalu.api.v1.views import list_elements, list_presence, person, list_sensors, sensor, list_complex_sensor

#-----------------------------------------------------------------------------

urlpatterns = [
  re_path(r'^$', list_elements, {'subpages': ['person', 'sensor']}),
  re_path(r'^person/?$', list_presence),
  re_path(r'^person/(?P<nick>.+)$', person),
  re_path(r'^sensor/?$', list_sensors),
  re_path(r'^sensor/(?P<sensor_id>[^/]+)/?$', sensor),
  re_path(r'^sensor/(?P<sensor_id>[^/]+)/(?P<sensor_subid>.+)$', list_complex_sensor),
  re_path(r'^.*', 'error_404'),
)

#-----------------------------------------------------------------------------
# vim:ft=python:nowrap:foldmethod=marker
