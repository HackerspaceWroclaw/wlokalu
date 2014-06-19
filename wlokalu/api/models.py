#!/usr/bin/python

from django.db import models

#-----------------------------------------------------------------------------

class Person(models.Model):
  nick = models.CharField(max_length = 256, primary_key = True)
  since = models.DateTimeField(auto_now_add = True)

#-----------------------------------------------------------------------------

class Sensor(models.Model):
  sensor_id = models.CharField(max_length = 256, primary_key = True)
  state = models.CharField(max_length = 256)
  since = models.DateTimeField(auto_now_add = True)

#-----------------------------------------------------------------------------

# this class is used like this:
#   sensor = models.ListSensor('/')
#   sensor.name = 'xxx'
#   sensor.subname = 'yyy'
#   sensor.save()
#
#   models.ListSensor.objects.filter(sensor_id__startswith = 'xxx/')
#   models.ListSensor.objects.filter(sensor_id__endswith = '/yyy')

class ListSensor(models.Model):
  # sensor_id is an artificial key composed of name and subname
  sensor_id = models.CharField(max_length = 512, primary_key = True)
  since = models.DateTimeField(auto_now_add = True)

  @property
  def name(self):
    return self.sensor_id.split('/', 1)[0]

  @name.setter
  def name(self, new_name):
    self.sensor_id = "%s/%s" % (new_name, self.subname)

  @property
  def subname(self):
    return self.sensor_id.split('/', 1)[1]

  @subname.setter
  def subname(self, new_subname):
    self.sensor_id = "%s/%s" % (self.name, new_subname)

#-----------------------------------------------------------------------------
# vim:ft=python:nowrap:foldmethod=marker
