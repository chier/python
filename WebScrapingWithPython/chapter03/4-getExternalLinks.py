#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Filename: 4-getExternalLinks
# @Date    : 2017-06-19 12:16
# @Author  : zzl
"""
   python_version  2.7.11
"""

from urllib2 import urlopen
from urllib2 import URLError,HTTPError
from urlparse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

#获取页面所有内链的列表
def getInternalLinks(bsObj,includeUrl):
    includeUrl = urlparse(includeUrl).scheme + "://" + urlparse(includeUrl).netloc
    internalLinks = []
    #找出所有以 "/" 开头的链接 '‘'
    for link in bsObj.findAll("a",href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if link.attrs['href'].startswitch("/"):
                    internalLinks.append(includeUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks

#获取页面的所有外链的列表
def getExternalLinks(bsObj,excludeUrl):
    externalLinks = []
    #找出所有以 "http"或"www"开头且包含当前URL的链接
    for link in bsObj.findAll("a",href=re.compile(
        "^(http|www)((?!"+excludeUrl+").)*$" )):
        if link.attrs['href'] is not None:
            if link.attrs["href"] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def getRandomExternalLink(startimgPage):
    try:
        html = urlopen(startimgPage)
    except URLError as e:
        print(startimgPage + " URLError")
        return None
    bsObj = BeautifulSoup(html,"html5lib")
    externalLinks = getExternalLinks(bsObj,urlparse(startimgPage).netloc)
    if len(externalLinks) == 0:
        print("No external links ,looking around the site for one")
        domain = urlparse(startimgPage).scheme + "://" + urlparse(startimgPage).netloc
        internalLinks = getInternalLinks(bsObj,domain)
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks) -1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks) -1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    if externalLink != None:
        print("Random external link is: " + externalLink)
        followExternalOnly(externalLink)
    else:
        print(None)

followExternalOnly("https://www.oreilly.com/")






















