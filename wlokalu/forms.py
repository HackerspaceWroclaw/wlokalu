#!/usr/bin/python

from django import forms
#from django.core.exceptions import ValidationError

#-----------------------------------------------------------------------------

class PresenceForm(forms.Form):
  nick = forms.CharField(
    label = "nick",
    widget = forms.TextInput(attrs = {'class': 'nick'}),
  )

#-----------------------------------------------------------------------------
# vim:ft=python
