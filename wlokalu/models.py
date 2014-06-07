#!/usr/bin/python

from django.db import models

#-----------------------------------------------------------------------------

class Person(models.Model):
  nick = models.CharField(max_length = 256, primary_key = True)

#-----------------------------------------------------------------------------
# vim:ft=python:nowrap:foldmethod=marker
