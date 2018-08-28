#!/usr/bin/env python
# excercise of use web api to acquire and analyse 
# data from web sites.

import requests
import json

url = 'https://xinwangus.blogspot.com/'
resp = requests.get(url)
print("status:", resp.status_code)
# now use json format
#resp_dict = resp.json()


print(resp.text)


