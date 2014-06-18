#!/usr/bin/python

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import django.shortcuts
import json

from wlokalu.api import presence

#-----------------------------------------------------------------------------

@csrf_exempt
def person(request, nick):
  context = {
    'address': request.META['REMOTE_ADDR'],
    'uri': request.META['REQUEST_URI'],
  }

  if request.method == "PUT":
    presence.person_entered(nick, context)
    reply = {"status": "ok"}
  elif request.method == "DELETE":
    presence.person_left(nick, context)
    reply = {"status": "ok"}
  elif request.method == "GET":
    person = presence.person(nick)
    if person:
      reply = {"status": "ok", "since": person.since}
    else:
      reply = {"status": "not found"}
  else:
    return HttpResponse(status = 405)

  return HttpResponse(json.dumps(reply) + "\n", content_type = "text/json")

@csrf_exempt
def sensor(request, sensor_id):
  context = {
    'address': request.META['REMOTE_ADDR'],
    'uri': request.META['REQUEST_URI'],
  }

  if request.method == "POST":
    reply = {"status": "TODO"}
  elif request.method == "DELETE":
    reply = {"status": "TODO"}
  elif request.method == "GET":
    reply = {"status": "TODO"}
  else:
    return HttpResponse(status = 405)

  return HttpResponse(reply, content_type = "text/json")

#-----------------------------------------------------------------------------
# vim:ft=python:foldmethod=marker
