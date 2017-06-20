#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
   python_version  2.7.11
   autho zzl
"""
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"html5lib")
images = bsObj.findAll("img",{"src" : re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image)