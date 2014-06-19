#!/usr/bin/python

from wlokalu.logging import getLogger, message
logger = getLogger('wlokalu.presence')

from models import Person, SimpleSensor, ComplexSensor

#-----------------------------------------------------------------------------

def log(*args, **kwargs):
  context = kwargs.get('context')
  if context is not None:
    del kwargs['context']
    kwargs.update(context)
  return message(*args, **kwargs)

#-----------------------------------------------------------------------------

def person_entered(nick, context = None):
  if Person.objects.filter(nick = nick).count() == 0:
    Person(nick).save() # add if not exists
    logger.info(log('person entered premises', nick = nick, context = context))

def person_left(nick, context = None):
  people = Person.objects.filter(nick = nick)
  if people.count() > 0:
    people.delete()
    logger.info(log('person left premises', nick = nick, context = context))

def person(nick):
  people = Person.objects.filter(nick = nick)
  if people.count() == 0:
    return None
  else:
    return people[0]

def list_people():
  return Person.objects.all().order_by('nick')

#-----------------------------------------------------------------------------

def sensor_state(sensor_id, state, context = None):
  if isinstance(state, (list, tuple)):
    return complex_sensor_update(sensor_id, state, context)
  else:
    return simple_sensor_update(sensor_id, state, context)

def simple_sensor(sensor_id):
  sensors = SimpleSensor.objects.filter(sensor_id = sensor_id)
  if sensors.count() == 0:
    return None
  else:
    return sensors[0]

def list_simple_sensors():
  return SimpleSensor.objects.all().order_by('sensor_id')

def complex_sensor(sensor_id):
  sensors = \
    ComplexSensor.objects.filter(sensor_id__startswith = "%s/" % (sensor_id,))
  if sensors.count() == 0:
    return None
  else:
    return sensors

def complex_sensor_field(sensor_id, sensor_subid):
  name = "%s/%s" % (sensor_id, sensor_subid)
  sensors = ComplexSensor.objects.filter(sensor_id = name)
  if sensors.count() == 0:
    return None
  else:
    return sensors[0]

def list_complex_sensors():
  sensors = {}
  order = []
  for s in ComplexSensor.objects.all().order_by('sensor_id'):
    entry = {
      'name': s.subname,
      'since': s.since,
    }
    if s.name not in sensors:
      sensors[s.name] = { 'name': s.name, 'entries': [entry] }
      order.append(s.name)
    else:
      sensors[s.name]['entries'].append(entry)
  return [sensors[s] for s in order]

def delete_sensor(sensor_id, context = None):
  sensors = SimpleSensor.objects.filter(sensor_id = sensor_id)
  list_sensors = \
    ComplexSensor.objects.filter(sensor_id__startswith = "%s/" % (sensor_id,))
  if sensors.count() > 0 or list_sensors.count() > 0:
    sensors.delete()
    list_sensors.delete()
    logger.info(log('deleted sensor', sensor = sensor_id, context = context))

#-----------------------------------------------------------------------------

def complex_sensor_update(sensor_id, states, context = None):
  sensors = \
    ComplexSensor.objects.filter(sensor_id__startswith = "%s/" % (sensor_id,)) \
                         .order_by('sensor_id')
  existing = set([s.subname for s in sensors])
  incoming = set(states)
  states = sorted(states)

  added = []
  for s in states:
    if s not in existing:
      added.append(s)
      ComplexSensor('%s/%s' % (sensor_id, s)).save()

  deleted = []
  for s in sensors:
    if s.subname not in incoming:
      deleted.append(s.subname)
      s.delete()

  if len(added) + len(deleted) > 0:
    update = {
      'all': states,
      'added': added,
      'deleted': deleted,
    }
    logger.info(log('updated sensor', sensor = sensor_id, update = update,
                    context = context))

def simple_sensor_update(sensor_id, state, context = None):
  sensors = SimpleSensor.objects.filter(sensor_id = sensor_id)
  if sensors.count() > 0:
    sensor = sensors[0]
  else:
    sensor = SimpleSensor(sensor_id = sensor_id)
  if sensor.state != state:
    sensor.state = state
    sensor.save()
    logger.info(log('updated sensor', sensor = sensor_id, state = state,
                    context = context))

#-----------------------------------------------------------------------------
# vim:ft=python:foldmethod=marker
