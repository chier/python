#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Filename: 2-crawlWikipedia
# @Date    : 2017-06-19 11:30
# @Author  : zzl
"""
   python_version  2.7.11
"""
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re  #正则表达式工具包

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html,"html5lib")
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing smoething! No worries though!")

    for link in bsObj.findAll("a",href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print("----------------\n" + newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("")
















