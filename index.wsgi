#!/usr/bin/python

import os
import sys

_path = os.path.dirname(__file__)
if _path not in sys.path:
  sys.path.append(_path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'wlokalu.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
