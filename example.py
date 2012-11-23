#!/usr/bin/env python
import requests
import json

params = {
	'q' : 'subtitle:walfang',
	'limit' : '100',
	'fields' : 'subtitle,uri'
}

url = 'http://api.zeit.de/content?'
headers = {'X-Authorization': '[ZEIT_API_KEY_HERE]'}

r = requests.get(url, params=params, headers=headers)

json = r.json

for result in json['matches']:
	print result['subtitle']
	print result['uri']
	print 


