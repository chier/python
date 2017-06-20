#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
   python_version  2.7.11
   autho zzl
   使用 urllib2 的 urlopen
"""

from urllib2 import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())