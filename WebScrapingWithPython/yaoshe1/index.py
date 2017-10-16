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
import requests
# import urllib
import re
import os

downLoadFile = 'H:\\happy\\5\\' ##要下载到的目录

def getFile(url):
    if(requests.get(url).status_code == 404):
        print('这是个错误网址')
        return []
    #print ('正在打开 ',url)
    file_name = url.split('/')[-1]
    file_s = downLoadFile  + file_name
    if os.path.exists(file_s):
        print("file exists = " + file_name)
        return
    u = urlopen(url)
    # u = requests.urlopen(url)

    f = open(file_s, 'wb')

    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        f.write(buffer)
    f.close()
    print("Sucessful to download = " + file_name)

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
    urls = re.findall(r"(http://www.yaoshe2.com/get_file/.*?mp4).*?",ss,re.I)
    for i in urls:
        print(i)
        try:
        	getFile(i);
        except Exception,e:
            print e.message
    # else:
        # print 'this is over'
    # bsObj = BeautifulSoup(html, "html5lib")
    # print bsObj

def eachLatestUpdates():
    print "eachLatestUpdates"
    while currPage < 10:
        startOpenPage("http://www.yaoshe2.com/latest-updates/" + currPage + "/")
        currPage = currPage +1




def startOpenPage(url):
    html = urlopen(url)
    # print(html.read())
    bsObj = BeautifulSoup(html, "html5lib")
    itemsDivObj = bsObj.findAll("div",{"class":re.compile("^(item)((?!:).)*$")})
    print "itemsDivObj div  item  = ",len(itemsDivObj)
    for obj in itemsDivObj:
        videosObjs = obj.findAll("a",{"href":re.compile("^(http://www.yaoshe2.com/videos/)((?!:).)*$")})
        print "videosObjs a  videos  = ",len(videosObjs)
        if len(videosObjs) != 0:
            strHref = videosObjs[0].attrs["href"]
            # print strHref
            count = 0
            while count < 1:
                count = count+1
                print("url = " + strHref)
                opeVideoUrl(strHref)


currPage = 2
startOpenPage("http://www.yaoshe2.com/")
eachLatestUpdates()





