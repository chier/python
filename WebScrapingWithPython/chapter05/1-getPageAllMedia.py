#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Filename: 1-getPageAllMedia
# @Date    : 2017-06-20 10:56
# @Author  : zzl
"""
   python_version  2.7.11
"""

import os
from urllib2 import urlopen
from urllib import urlretrieve
from urlparse import urlparse
from bs4 import BeautifulSoup

downloadDirectory = "downloaded"
baseUrl = "http://www.27270.com"
downUrl = "http://www.27270.com/tag/320.html"
def getAbsoluteURL(baseUrl,source):
    # if source.startswith("http://www."):
    #     url = "http://" + source[11:]
    # elif source.startswith("http://"):
    #     url = source
    # elif source.startswith("www"):
    #     url = "http://" + source[4:]
    # else:
    #     url = baseUrl + "/" + source
    url = source
    # if baseUrl not in url:
        # return None
    return url

def getDownloadPath(baseUrl,absoluteUrl,downloadDirectory):
    path = absoluteUrl.replace("www","")
    path = path.replace(baseUrl,"")
    path = path.split("com/")[-1]

    path = downloadDirectory +"/"+ path
    directory = os.path.dirname(path)
    u = urlparse(path)
    qs = u.query
    fileName = path.replace('?'+ qs,'')
    print("directory = " + directory)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return fileName

html = urlopen(downUrl)
bsObj = BeautifulSoup(html,"html5lib")
downloadList = bsObj.findAll("img",src=True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl,download["src"])
    if fileUrl is not None:
        print(fileUrl)
        filepath =  getDownloadPath(baseUrl,fileUrl,downloadDirectory)
        print("filepath = " + filepath)
        # filepath = "downloaded/jquery.js?v1"
        urlretrieve(fileUrl,filepath)

