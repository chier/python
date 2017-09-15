#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Filename: index
# @Date    : 2017-09-14 23:15
# @Author  : zzl
"""
   python_version  2.7.11
"""
from urllib2 import urlopen
# from urllib2 import open
from bs4 import BeautifulSoup
import urllib2
import re

def opeVideoUrl(url):
    html = urlopen(url).read()
    ss = html.replace(" ","")
    urls = re.findall(r"(http://www.yaoshe1.com/get_file/.*?mp4).*?",ss,re.I)
    for i in urls:
        print i
        # urllib2.urlretrieve(i, "%s.mp4" % (i, ))
    # else:
        
        # print 'this is over'
    # bsObj = BeautifulSoup(html, "html5lib")
    # print bsObj


html = urlopen("http://www.yaoshe1.com/")
# print(html.read())
bsObj = BeautifulSoup(html, "html5lib")
itemsDivObj = bsObj.findAll("div",{"class":re.compile("^(item)((?!:).)*$")})
for obj in itemsDivObj:
    videosObjs = obj.findAll("a",{"href":re.compile("^(http://www.yaoshe1.com/videos/)((?!:).)*$")})
    # print("==================")
    strHref = videosObjs[0].attrs["href"]
    # print strHref
    count = 0
    while count < 1:
        count = count+1
        opeVideoUrl(strHref)




