#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Filename: 2-getUtf8Text
# @Date    : 2017-06-20 17:21
# @Author  : zzl
"""
   python_version  2.7.11
"""

from zipfile import ZipFile
from urllib2 import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')

wordObj = BeautifulSoup(xml_content.decode('utf-8'),"lxml")
textStrings = wordObj.findAll("w:t")
for textElem in textStrings:
    print(textElem.text)