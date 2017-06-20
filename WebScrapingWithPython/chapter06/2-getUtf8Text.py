#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Filename: 2-getUtf8Text
# @Date    : 2017-06-20 17:21
# @Author  : zzl
"""
   python_version  2.7.11
"""

from urllib2 import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
print "geturl=",html.geturl()
print "info=",html.info()
print(html)
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
content = bytes(content, "UTF-8")
content = content.decode("UTF-8")
print(content)