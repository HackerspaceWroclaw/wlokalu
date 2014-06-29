#!/usr/bin/python
#
# An example of how to submit data about simple sensor.
#
#-----------------------------------------------------------------------------

import sys
import httplib
import urlparse
import json

#-----------------------------------------------------------------------------

class WLokalu:
  def __init__(self, url):
    urlp = urlparse.urlparse(url)
    self.host = urlp.hostname
    self.port = urlp.port
    self.app_path = urlp.path.rstrip('/')

  def request(self, method, path, body = None):
    h = httplib.HTTPConnection(host = self.host, port = self.port)
    if body is not None:
      h.request(method, path, json.dumps(body))
    else:
      h.request(method, path)

    resp = h.getresponse()
    if resp.status / 100 == 2:
      return json.loads(resp.read())
    else:
      raise Exception('HTTP error %d' % (resp.status,))

  def get(self, sensor):
    path = '%s/api/v1/sensor/%s' % (self.app_path, sensor)
    return self.request('GET', path)

  def put(self, sensor, state):
    path = '%s/api/v1/sensor/%s' % (self.app_path, sensor)
    return self.request('POST', path, {"state": state})

  def delete(self, sensor):
    path = '%s/api/v1/sensor/%s' % (self.app_path, sensor)
    return self.request('DELETE', path)

#-----------------------------------------------------------------------------

if len(sys.argv) < 3 or sys.argv[1] in ('-h', '--help'):
  print "Usage:"
  print "  %s http://wlokalu.hswro.org/ sensor-name state" % (sys.argv[0])
  print "  %s http://wlokalu.hswro.org/ sensor-name" % (sys.argv[0])
  sys.exit()

if len(sys.argv) == 3:
  url = sys.argv[1]
  sensor = sys.argv[2]
  state = None
else:
  url = sys.argv[1]
  sensor = sys.argv[2]
  state = sys.argv[3]

wlokalu = WLokalu(url)
if state is not None:
  wlokalu.put(sensor, state)
else:
  wlokalu.delete(sensor)
