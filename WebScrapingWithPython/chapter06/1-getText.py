#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Filename: 1-getText
# @Date    : 2017-06-20 17:16
# @Author  : zzl
"""
   python_version  2.7.11
"""
from urllib2 import urlopen
textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
print(textPage.read())