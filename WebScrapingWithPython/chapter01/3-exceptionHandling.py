#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
   python_version  2.7.11
   autho zzl
   增加异常处理 ，增加 html5lib HTML解析库
"""
from urllib2 import urlopen
from urllib2 import HTTPError,URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except(HTTPError,URLError) as e:
        return None
    try:
        htmlCode = html.read()
        print(htmlCode)
        bsObj = BeautifulSoup(htmlCode, "html5lib")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("title could not be found")
else:
    print(title)


title1 = getTitle("http://www.pythonscraping.com/pages/page1.html1")
if title1 == None:
    print("title could not be found")
else:
    print(title1)
