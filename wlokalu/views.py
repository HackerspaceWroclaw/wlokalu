#!/usr/bin/python

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt

from wlokalu.logging import getLogger, message as log

from models import Person

#-----------------------------------------------------------------------------

def person_enter(nick):
  Person(nick).save()

def person_leave(nick):
  Person(nick).delete()

def list_people():
  return Person.objects.all().order_by('nick')

#-----------------------------------------------------------------------------

@csrf_exempt
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
      person_enter(request.POST['nick'])
    else: # 'leave' in request.POST
      person_leave(request.POST['nick'])

  context = RequestContext(request, {
    'form_target': form_target,
    'form': form,
    'present': list_people(),
  })
  return HttpResponse(template.render(context))

#-----------------------------------------------------------------------------

def hello_world(request):
  template = loader.get_template("hello_world.html")
  context = RequestContext(request, {})
  return HttpResponse(template.render(context))

#-----------------------------------------------------------------------------
# vim:ft=python:foldmethod=marker
