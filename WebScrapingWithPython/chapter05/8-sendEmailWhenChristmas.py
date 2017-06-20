#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Filename: 8-sendEmailWhenChristmas
# @Date    : 2017-06-20 17:06
# @Author  : zzl
"""
   python_version  2.7.11
"""

import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib2 import urlopen
import time

def sendMail(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "christmas_alerts@pythonscraping.com"
    msg['To'] = "ryan@pythonscraping.com"

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"))
while(bsObj.find("a", {"id":"answer"}).attrs['title'] == "NO"):
    print("It is not Christmas yet.")
    time.sleep(3600)
    bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"))
sendMail("It's Christmas!", "According to http://itischristmas.com, it is Christmas!")
