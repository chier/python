#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
   python_version  2.7.11
   autho zzl
"""

from urllib2 import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# print(html.read())
bsObj = BeautifulSoup(html,"html5lib")

for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)

for previous in bsObj.find("table",{"id":"giftList"}).tr.previous_siblings:
    print(previous)
