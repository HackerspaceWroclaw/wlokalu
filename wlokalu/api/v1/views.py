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
def list_elements(request, subpages):
  return subpages

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
    return list_person(request, nick)

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
    return list_sensor(request, sensor_id)

  return HttpResponse(status = 405) # method not allowed

#-----------------------------------------------------------------------------

@csrf_exempt
@return_json
def list_presence(request):
  if request.method != "GET":
    return HttpResponse(status = 405) # method not allowed
  return [p.nick for p in presence.list_people()]

@csrf_exempt
@return_json
def list_person(request, nick):
  person = presence.person(nick)
  if person:
    return {
      "nick": nick,
      "present": True,
      "since": int(person.since.strftime("%s")), # no way to turn into epoch?
    }
  else:
    return {
      "nick": nick,
      "present": False,
      "since": None,
    }

@csrf_exempt
@return_json
def list_sensors(request):
  if 'simple' in request.GET:
    return [s.sensor_id for s in presence.list_simple_sensors()]
  elif 'complex' in request.GET:
    complex_list = set([s['name'] for s in presence.list_complex_sensors()])
    return sorted(complex_list)
  else:
    complex_list = set([s['name'] for s in presence.list_complex_sensors()])
    return [s.sensor_id for s in presence.list_simple_sensors()] + \
           sorted(complex_list)

@csrf_exempt
@return_json
def list_sensor(request, sensor_id):
  sensor = presence.simple_sensor(sensor_id)
  if sensor is not None:
    return {
      "sensor_id": sensor_id,
      "state": sensor.state,
      "since": int(sensor.since.strftime("%s")), # no way to turn into epoch?
    }

  sensor = presence.complex_sensor(sensor_id)
  if sensor is None:
    return {
      "sensor_id": sensor_id,
      "state": None,
      "since": None,
    }

  return [s.subname for s in sensor]

@csrf_exempt
@return_json
def list_complex_sensor(request, sensor_id, sensor_subid):
  if request.method != "GET":
    # updating single field in a complex sensor is disallowed (at least
    # currently; this might change in the future)
    return HttpResponse(status = 405) # method not allowed

  field = presence.complex_sensor_field(sensor_id, sensor_subid)
  if field:
    return {
      "sensor_id": sensor_id,
      "field": sensor_subid,
      "present": True,
      "since": int(field.since.strftime("%s")), # no way to turn into epoch?
    }
  else:
    return {
      "sensor_id": sensor_id,
      "field": sensor_subid,
      "present": False,
      "since": None,
    }

#-----------------------------------------------------------------------------
# vim:ft=python:foldmethod=marker
