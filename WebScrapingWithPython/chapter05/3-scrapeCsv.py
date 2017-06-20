#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Filename: 3-scrapeCsv
# @Date    : 2017-06-20 11:50
# @Author  : zzl
"""
   python_version  2.7.11
"""

import csv
from urllib2 import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, "html.parser")
#The main comparison table is currently the first table on the page
table = bsObj.findAll("table",{"class":"wikitable"})[0]
rows = table.findAll("tr")

csvFile = open("files/editors.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
try:
	for row in rows:
		csvRow = []
		for cell in row.findAll(['td', 'th']):
			csvRow.append(cell.get_text())
		writer.writerow(csvRow)
finally:
    csvFile.close()
