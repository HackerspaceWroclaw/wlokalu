#!/usr/bin/python

import os
import sys

_path = os.path.dirname(__file__)
if _path not in sys.path:
  sys.path.append(_path)

os.environ.setdefault['DJANGO_SETTINGS_MODULE'] = 'wlokalu.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
