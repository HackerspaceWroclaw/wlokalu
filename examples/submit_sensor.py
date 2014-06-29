#!/usr/bin/python
#
# An example of how to submit data about simple sensor.
#

import sys
import httplib
import urlparse
import json

if len(sys.argv) < 3 or sys.argv[1] in ('-h', '--help'):
  print "Usage:"
  print "  %s http://wlokalu.hswro.org/ sensor-name state" % (sys.argv[0])
  print "  %s http://wlokalu.hswro.org/ sensor-name" % (sys.argv[0])
  sys.exit()

if len(sys.argv) == 3:
  url = urlparse.urlparse(sys.argv[1])
  sensor = sys.argv[2]
  state = None
else:
  url = urlparse.urlparse(sys.argv[1])
  sensor = sys.argv[2]
  state = sys.argv[3]

h = httplib.HTTPConnection(host = url.hostname, port = url.port)
if url.path.endswith('/'):
  path = '%sapi/v1/sensor/%s' % (url.path, sensor)
else:
  path = '%s/api/v1/sensor/%s' % (url.path, sensor)

if state is None:
  h.request('DELETE', path)
else:
  h.request('POST', path, json.dumps({"state": state}))

resp = h.getresponse()
if resp.status / 100 == 2:
  print "OK"
  print resp.read().strip()
else:
  print "failed"
