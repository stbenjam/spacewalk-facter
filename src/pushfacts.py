#!/usr/bin/env python

""" Push Facter facts to RHN Satellite """

import os
import sys
import json
import socket
import urllib2
import urlparse
import xmlrpclib

# RHN imports
sys.path.append("/usr/share/rhn/")
import up2date_client.config

# Satellite Hostname:
satellite = urlparse.urlparse(up2date_client.config.getServerlURL()[0]).hostname

# Post URL to push Our Facts:
postURL   = "http://%s/cgi-bin/postfacts.py" % satellite

# Fetch the RHN System ID:
systemID  = xmlrpclib.loads(open("/etc/sysconfig/rhn/systemid").read())[0][0]['system_id'].split('-')[1]

# Fetch Facts
facts = dict(item.split(" => ") for item in os.popen('/usr/bin/facter').read().splitlines())
facts['systemID'] = systemID

facts = json.dumps(facts)

# Push Facts
socket.setdefaulttimeout(15)
try:
    request  = urllib2.Request(postURL, facts, {'Content-Type': 'application/json'})
    f = urllib2.urlopen(request)
    response = f.read()
    f.close()
except urllib2.URLError:
    print "Couldn't connect to Satellite server."
    sys.exit()

print response
