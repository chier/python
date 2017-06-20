#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Filename: 1-getPageMedia
# @Date    : 2017-06-20 10:51
# @Author  : zzl
"""
   python_version  2.7.11
"""

from urllib import urlretrieve
from urllib2 import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html,"html5lib")
imageLocation = bsObj.find("a",{"id":"logo"}).find("img")["src"]
urlretrieve(imageLocation,"logo.jpg")
