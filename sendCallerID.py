#!/usr/bin/python
# Copyright (C) 2013 Mike O'Driscoll <mike@mikeodriscoll.ca>

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
import json
import urllib
import urllib2

if( len(sys.argv) < 3 ):
	sys.exit(1)

#Replace your XBMC URL HERE
XBMCurl = "http://user:pass@ip:port"
jsonRPCUrl = XBMCurl + '/jsonrpc'

#Specify the content type as JSON otherwise XBMC will ignore.
headers = {}
headers['Content-Type'] = 'application/json'
#Generate the python dict representing the request
jsonDict = {'jsonrpc':"2.0", 'method':"GUI.ShowNotification",'params':{'title':"Incomming Call",'message':sys.argv[1] + " " + sys.argv[2]}, 'id':1}
json = json.dumps(jsonDict)
post_data = json.encode('utf-8')

#Generate the request with headers and send it
req = urllib2.Request(jsonRPCUrl, post_data, headers)
urllib2.urlopen(req)

