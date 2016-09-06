#coding=utf-8
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    print html
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    print "下载图片"
    for imgurl in imglist:
        print imgurl
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1
    return imglist


html = getHtml("http://tieba.baidu.com/p/4766061066")

print getImg(html)