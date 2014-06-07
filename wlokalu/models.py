#!/usr/bin/python

from django.db import models

#-----------------------------------------------------------------------------

class Person(models.Model):
  nick = models.CharField(max_length = 256, primary_key = True)
  since = models.DateTimeField(auto_now_add = True)

#-----------------------------------------------------------------------------
# vim:ft=python:nowrap:foldmethod=marker
