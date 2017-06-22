#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
   python_version  2.7.11
   autho zzl
"""
import json
from urllib2 import urlopen

def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")

print(getCountry("50.78.253.58"))