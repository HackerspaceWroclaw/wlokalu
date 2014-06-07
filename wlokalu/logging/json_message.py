#!/usr/bin/python

import ordereddict
import json

#-----------------------------------------------------------------------------
# class Message(OrderedDict) {{{

class Message(ordereddict.OrderedDict):
  def __str__(self):
    return json.dumps(self)

# }}}
#-----------------------------------------------------------------------------
# message('log message', (key, value), key = value) {{{

def message(*args, **kwargs):
  args = list(args)
  if len(args) > 0 and type(args[0]) != tuple:
    args[0] = ('message', args[0])

  msg = Message(args)
  keys = kwargs.keys()
  keys.sort()
  for k in keys:
    msg[k] = kwargs[k]

  return msg

# }}}
#-----------------------------------------------------------------------------
# vim:ft=python:foldmethod=marker
