import os
import sys
import json
import httplib, urllib
import base64
import string

#sys.stdout = open(os.path.join(tempfile.gettempdir(), 'stdout'), 'a')
#sys.stderr = open(os.path.join(tempfile.gettempdir(), 'stderr'), 'a')

dir = os.path.join(os.path.join(os.environ.get('SPLUNK_HOME')), 'etc', 'apps', 'alert_webhook_plus', 'bin', 'lib')
if not dir in sys.path:
  sys.path.append(dir)

from CsvResultParser import *
from urlparse import urlparse

def getResults(results_file):
  parser = CsvResultParser(results_file)
  results = parser.getResults()
  return results

if sys.argv[1] == "--execute":
  payload = json.loads(sys.stdin.read())
  print >> sys.stderr, "INFO Payload: %s" % json.dumps(payload)

  params = payload.get('configuration')

  if "http.user" not in params or params["http.user"] == "" or "http.password" not in params or params["http.password"] == "" or "http.url" not in params or params["http.url"] == "":
    print >> sys.stderr, "FATAL Missing required params, exit."
    sys.exit(1)

  else:
  
    auth = base64.encodestring('%s:%s' % (params["http.user"],  params["http.password"])).replace('\n','')
  
    url = urlparse(params['http.url']) 
    
    if url.scheme == "http":		
      conn = httplib.HTTPConnection(url.netloc)
    elif url.scheme == "https":
      conn = httplib.HTTPSConnection(url.netloc)
    else:
      print >> sys.stderr, "FATAL No valid scheme found, exit."
      sys.exit(1)


    # Getting results dict
    results = getResults(payload.get('results_file'))

    # Removing unneded elements
    del payload['result']
    del payload['configuration']
 
    # Adding results dict to payload
    payload.update({"results": results})

    results = getResults(payload.get('results_file'))
 
    conn.putrequest("POST", url.path, urllib.urlencode(payload))
    conn.putheader("Authorization", "Basic %s" % auth)
    conn.putheader("Content-type", "application/json")
    conn.endheaders()
    response = conn.getresponse()
    data = response.read()
    conn.close()

#    with open("/tmp/webhook_plus_payload.log", "a") as myfile:
#      myfile.write(json.dumps(payload))
#      myfile.write("\n")
#      myfile.write(url.path)
#      myfile.write("\n")
#      myfile.close()

    print >> sys.stderr, "INFO Status: %s" % response.status
    print >> sys.stderr, "INFO Reason: %s" % response.reason
