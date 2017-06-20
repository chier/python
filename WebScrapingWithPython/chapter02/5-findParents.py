#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
   python_version  2.7.11
   autho zzl
"""

from urllib2 import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"html5lib")
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"
                        }).parent.previous_sibling.get_text())
