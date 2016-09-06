#coding=utf-8
from bs4 import BeautifulSoup
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://tieba.baidu.com/p/4766061066")
soup = BeautifulSoup(html)
print(soup.prettify())
print html