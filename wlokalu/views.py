#!/usr/bin/python

from django.http import HttpResponse
from django.template import RequestContext, loader
from wlokalu.logging import getLogger, message as log

#-----------------------------------------------------------------------------

def list(request, nick = None):
  template = loader.get_template("list.html")

  from django.core.urlresolvers import reverse
  from forms import PresenceForm
  form = PresenceForm()
  if nick is not None:
    form.initial['nick'] = nick
    form_target = reverse(list, kwargs = {'nick': nick})
  else:
    form_target = reverse(list)

  if request.POST.get('nick', '') != '':
    if 'enter' in request.POST:
      msg = "%s enters HS" % (request.POST['nick'])
    else: # 'leave' in request.POST
      msg = "%s leaves HS" % (request.POST['nick'])
  else:
    msg = None

  context = RequestContext(request, {
    'form_target': form_target,
    'form': form,
    'msg': msg,
  })
  return HttpResponse(template.render(context))

#-----------------------------------------------------------------------------

def hello_world(request):
  template = loader.get_template("hello_world.html")
  context = RequestContext(request, {})
  return HttpResponse(template.render(context))

#-----------------------------------------------------------------------------
# vim:ft=python:foldmethod=marker
