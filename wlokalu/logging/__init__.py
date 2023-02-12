#!/usr/bin/python

import logging
import logging.config
from django.conf import settings

from .json_message import message

#-----------------------------------------------------------------------------
# dictConfig() {{{

if hasattr(logging.config, 'dictConfig'):
  # Python 2.7+
  dictConfig = logging.config.dictConfig
else:
  # older, use local copy of dictConfig()
  from . import logging_config
  dictConfig = logging_config.dictConfig

# }}}
#-----------------------------------------------------------------------------
# load configuration from YAML/JSON {{{

def _load_yaml(filename):
  import yaml
  return yaml.safe_load(open(filename))

def _load_json(filename):
  import json
  return json.load(open(filename))

# }}}
#-----------------------------------------------------------------------------
# exceptions {{{

class UnkownExtensionException(Exception):
  pass

# }}}
#-----------------------------------------------------------------------------
# setup {{{

def _load_config():
  if not hasattr(settings, 'WLOKALU_LOGGING_CONFIG') or \
     settings.WLOKALU_LOGGING_CONFIG == None:
    # no logging configured, ignore all logs
    return {
      'version': 1,
      'root': { 'handlers': ['null'] },
      'handlers': {
        'null': { 'class': 'wlokalu.logging.handlers.NullHandler' },
      },
    }
  elif isinstance(settings.WLOKALU_LOGGING_CONFIG, dict):
    return settings.WLOKALU_LOGGING_CONFIG
  elif settings.WLOKALU_LOGGING_CONFIG.endswith('.yaml') or \
       settings.WLOKALU_LOGGING_CONFIG.endswith('.yml'):
    return _load_yaml(settings.WLOKALU_LOGGING_CONFIG)
  elif settings.WLOKALU_LOGGING_CONFIG.endswith('.json'):
    return _load_json(settings.WLOKALU_LOGGING_CONFIG)
  else:
    raise UnkownExtensionException('Unknown extension for config %s' % \
                                   (settings.WLOKALU_LOGGING_CONFIG))

# }}}
#-----------------------------------------------------------------------------
# getLogger() {{{

# TODO: add sensible reloading log configuration (sensible means not on module
# import, as it can be once for long, long time under WSGI or FastCGI)

# FIXME: I'm not sure if this is correct way of setting up global
# configuration

log_config = None

def getLogger(*args, **kwargs):
  global log_config
  if not log_config:
    log_config = _load_config()
    dictConfig(log_config)

  return logging.getLogger(*args, **kwargs)

# }}}
#-----------------------------------------------------------------------------
# vim:ft=python:foldmethod=marker
