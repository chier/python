#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Filename: 1-getText
# @Date    : 2017-06-20 17:16
# @Author  : zzl
"""
   python_version  2.7.11
"""
"""
    ERROR:
    C:\Python27\python.exe G:/github.com/python/WebScrapingWithPython/chapter07/2-clean2grams.py
Traceback (most recent call last):
  File "G:/github.com/python/WebScrapingWithPython/chapter07/2-clean2grams.py", line 48, in <module>
    ngrams = getNgrams(content, 2)
  File "G:/github.com/python/WebScrapingWithPython/chapter07/2-clean2grams.py", line 31, in getNgrams
    input = cleanInput(input)
  File "G:/github.com/python/WebScrapingWithPython/chapter07/2-clean2grams.py", line 20, in cleanInput
    input = bytes(input, "UTF-8")
TypeError: str() takes at most 1 argument (2 given)

Process finished with exit code 1

"""
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
import string
import codecs
from collections import OrderedDict

def cleanInput(input):
    input = re.sub('\n+', " ", input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    # input = bytes(input, encoding="UTF-8")  python 3
    # input  = codecs.getreader("UTF-8")(input)
    input = input.encode("UTF-8") # python 2.7 编码方法
    input = input.decode("ascii", "ignore")
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def getNgrams(input, n):
    input = cleanInput(input)
    output = dict()
    for i in range(len(input)-n+1):
        newNGram = " ".join(input[i:i+n])
        if newNGram in output:
            output[newNGram] += 1
        else:
            output[newNGram] = 1
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
#ngrams = getNgrams(content, 2)
#print(ngrams)
#print("2-grams count is: "+str(len(ngrams)))

ngrams = getNgrams(content, 2)
ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
print(ngrams)