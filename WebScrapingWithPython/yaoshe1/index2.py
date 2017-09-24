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
# import urllib
import re

def getFile(url):
    file_name = url.split('/')[-1]
    u = urlopen(url)
    f = open(file_name, 'wb')

    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        f.write(buffer)
    f.close()
    print "Sucessful to download" + " " + file_name

def getHtml(url):
    page = urlopen(url)
    html = page.read()
    page.close()
    return html

# compile the regular expressions and find
# all stuff we need
def getUrl(html):
    reg = r'(?:href|HREF)="?((?:http://)?.+?\.pdf)'
    url_re = re.compile(reg)
    url_lst = re.findall(url_re,html)
    return(url_lst)

def opeVideoUrl(url):
    html = urlopen(url).read()
    ss = html.replace(" ","")
    urls = re.findall(r"(http://www.yaoshe1.com/get_file/.*?mp4).*?",ss,re.I)
    for i in urls:
        print i
        getFile(i);
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
        print("url = " + strHref)
        opeVideoUrl(strHref)



