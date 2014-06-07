#!/usr/bin/python

from django.http import HttpResponse
from django.template import RequestContext, loader
from wlokalu.logging import getLogger, message as log

#-----------------------------------------------------------------------------

def hello_world(request):
  template = loader.get_template("hello_world.html")
  context = RequestContext(request, {})
  return HttpResponse(template.render(context))

#-----------------------------------------------------------------------------
# vim:ft=python:foldmethod=marker
