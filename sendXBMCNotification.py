#!/usr/bin/python
# Copyright (C) 2013 Mike O'Driscoll <mike@mikeodriscoll.ca>
# Contributions by Greg Jacobs <http://github.com/gregwjacobs>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Quick utility for compiling a JSON object request for XBMC v12 (Frodo) 
that asterisk calls to send a caller ID notification
"""

import sys

# Support for older Python systems (< 2.6) which install simplejson as a workaround
# http://pypi.python.org/pypi/simplejson
try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        print "ERROR: You must install json or simplejson module!"
        sys.exit(1)
import urllib
import urllib2

USAGE = """Usage: sendNotification.py HOST TITLE MESSAGE
Send a notification to XBMC with a title of TITLE and 
a message containing MESSAGE.

HOST is an expected URL format of http://user:pass@ip:port
"""

# Get the HOST from command line arg
XBMCurl = sys.argv[1]

jsonRPCUrl = XBMCurl + '/jsonrpc'
#Specify the content type as JSON otherwise XBMC will ignore.
headers = {}
headers['Content-Type'] = 'application/json'


def SendNotification(titleStr, messageStr):
    #Generate the python dict representing the request
    jsonDict = {'jsonrpc':"2.0", 'method':"GUI.ShowNotification",'params':{'title':titleStr,'message':messageStr}, 'id':1}
    jsonData = json.dumps(jsonDict)
    post_data = jsonData.encode('utf-8')

    #Generate the request with headers and send it
    req = urllib2.Request(jsonRPCUrl, post_data, headers)
    urllib2.urlopen(req)

if __name__ == "__main__":
    if( len(sys.argv) != 4 ):
        print USAGE
        sys.exit(1)
    else:
        SendNotification(sys.argv[2], sys.argv[3])
