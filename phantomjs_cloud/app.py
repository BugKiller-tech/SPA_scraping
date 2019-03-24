# -*- coding: utf-8 -*-

# import urllib2

# phantom_cloud_key = "ak-n17f0-1gczz-zzkma-3tk5w-7629w"
# data = """{
# 	"url":"http://example.com",
# 	"renderType":"plainText"
# }"""

# url = "http://PhantomJScloud.com/api/browser/v2/{key}/".format(key=phantom_cloud_key)
# headers = {'content-type':'application/json'}
# req = urllib2.Request(url, data, headers)
# response = urllib2.urlopen(req)
# results = response.read()

# print(response)

import requests
import json
from pprint import pprint

phantom_cloud_key = "ak-n17f0-1gczz-zzkma-3tk5w-7629w"
phantom_request_url = "http://PhantomJScloud.com/api/browser/v2/{key}/".format(key=phantom_cloud_key)

data = {
	"url":"https://intersport.com.au/",
	"renderType":"html",
	# "outputAsJson": True
}
response = requests.post(phantom_request_url, json.dumps(data))

status_code = response.status_code
print(status_code)
if status_code == 200:
	print(response.text)
else:
	print('can not be crawled by the tool')