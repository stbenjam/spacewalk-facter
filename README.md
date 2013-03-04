spacewalk-facter
================

Simple python cgi-bin for syncing your facter facts
with custom key/value pairs in RHN Satellite or
Spacewalk.


Installation:
-------------

1. Put postfacts.conf in /etc on your satellite server, put Satellite credentials here

2. Put postfacts.py in /var/www/cgi-bin on your satellite server, mode 755

3. Put pushfacts.py on your system

4. Run pushfacts.py on a system with facter installed 
