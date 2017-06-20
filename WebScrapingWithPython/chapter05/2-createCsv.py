#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Filename: 2-createCsv
# @Date    : 2017-06-20 11:46
# @Author  : zzl
"""
   python_version  2.7.11
"""
import csv
#from os import open
csvFile = open("files/test.csv", 'w+')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow( (i, i+2, i*2))
finally:
    csvFile.close()