#!/usr/bin/python

""" Uses Satellite API to update System's Custom Info """

import cgi
import sys
import json
import xmlrpclib
import ConfigParser

print "Content-type: text/plain"
print ""

# Read Configuration
config = ConfigParser.ConfigParser()
config.readfp(open("/etc/postfacts.conf"))
username = config.get('postfacts', 'username', 0)
password = config.get('postfacts', 'password', 0)

# Read facts
facts = json.loads(sys.stdin.read())

# Get list of all keys
keys = []
for k, v in facts.iteritems():
    keys.append(k)

# Connect to Satellite
rhn = xmlrpclib.Server('http://localhost/rpc/api', verbose=0)
key = rhn.auth.login(username, password)

existing = rhn.system.custominfo.listAllKeys(key)
existing = [k['label'] for k in existing]

for k in keys:
    if k not in existing:
        rhn.system.custominfo.createKey(key, k, "Facter Fact")

rhn.system.setCustomValues(key,int(facts['systemID']),facts)

print "Custom info updated."
