#!/usr/bin/python

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
import django.shortcuts

from wlokalu.api import presence

#-----------------------------------------------------------------------------

from wlokalu.logging import getLogger, message as log
logger = getLogger(__name__)

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
    context = {
      'address': request.META['REMOTE_ADDR'],
      'uri': request.META['REQUEST_URI'],
    }
    if 'enter' in request.POST:
      presence.person_entered(request.POST['nick'], context)
    else: # 'leave' in request.POST
      presence.person_left(request.POST['nick'], context)
    # tell the browser to reload the page, but with GET request
    return django.shortcuts.redirect(request.path)

  context = RequestContext(request, {
    'form_target': form_target,
    'form': form,
    'present': presence.list_people(),
    'sensors': presence.list_simple_sensors(),
    'complex_sensors': presence.list_complex_sensors(),
  })
  return HttpResponse(template.render(context))

#-----------------------------------------------------------------------------
# vim:ft=python:foldmethod=marker
