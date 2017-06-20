#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Filename: 2-getUtf8Text
# @Date    : 2017-06-20 17:21
# @Author  : zzl
"""
   python_version  2.7.11
"""

from urllib2 import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
dataFile = StringIO(data)
dictReader = csv.DictReader(dataFile)

print(dictReader.fieldnames)

for row in dictReader:
    print(row)