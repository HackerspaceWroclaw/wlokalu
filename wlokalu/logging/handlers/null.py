#!/usr/bin/python

import logging

#-----------------------------------------------------------------------------
# null handler {{{

class NullHandler(logging.Handler):
  def __init__(self):
    logging.Handler.__init__(self)

  def emit(self, record):
    pass

  def handle(self, record):
    pass

  def createLock(self):
    return None

# }}}
#-----------------------------------------------------------------------------
# vim:ft=python:foldmethod=marker
