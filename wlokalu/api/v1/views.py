#!/usr/bin/python

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import django.shortcuts
import json

from wlokalu.api import presence

#-----------------------------------------------------------------------------

from wlokalu.logging import getLogger, message as log
logger = getLogger(__name__)

#-----------------------------------------------------------------------------

def return_json(function):
  def replacement(*args, **kwargs):
    reply = function(*args, **kwargs)
    if type(reply) in (dict, list, str, unicode):
      return HttpResponse(json.dumps(reply) + "\n", content_type = "text/json")
    return reply

  return replacement

#-----------------------------------------------------------------------------

@csrf_exempt
@return_json
def person(request, nick):
  context = {
    'address': request.META['REMOTE_ADDR'],
    'uri': request.META['REQUEST_URI'],
  }

  if request.method == "PUT" or request.method == "POST":
    presence.person_entered(nick, context)
    return {"status": "ok"}

  if request.method == "DELETE":
    presence.person_left(nick, context)
    return {"status": "ok"}

  if request.method == "GET":
    person = presence.person(nick)
    if person:
      return {"status": "ok", "since": person.since}
    else:
      return {"status": "not found"}

  return HttpResponse(status = 405) # method not allowed

@csrf_exempt
@return_json
def sensor(request, sensor_id):
  context = {
    'address': request.META['REMOTE_ADDR'],
    'uri': request.META['REQUEST_URI'],
  }

  if request.method == "POST":
    try:
      if hasattr(request, 'body'): # Django 1.4+
        payload = json.loads(request.body)
      else: # Django <1.4
        payload = json.loads(request.raw_post_data)
      sensor_state = payload['state']
    except Exception, e:
      logger.warn(log('bad request', exception = str(e), **context))
      return HttpResponse(status = 400) # bad request
    presence.sensor_state(sensor_id, sensor_state, context)
    return {"status": "ok"}

  if request.method == "DELETE":
    presence.delete_sensor(sensor_id, context)
    return {"status": "ok"}

  if request.method == "GET":
    return {"status": "TODO"}

  return HttpResponse(status = 405) # method not allowed

#-----------------------------------------------------------------------------
# vim:ft=python:foldmethod=marker
