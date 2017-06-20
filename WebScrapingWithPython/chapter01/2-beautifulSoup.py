#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
   python_version  2.7.11
   autho zzl
   使用 beautifulSoup bs4
"""
from urllib2 import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
htmlCode = html.read()
print(htmlCode +"\n")
bsObj = BeautifulSoup(htmlCode)
print(bsObj.h1)