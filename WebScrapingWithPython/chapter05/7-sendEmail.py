#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Filename: 7-sendEmail
# @Date    : 2017-06-20 17:04
# @Author  : zzl
"""
   python_version  2.7.11
"""

import smtplib
from email.mime.text import MIMEText

msg = MIMEText("The body of the email is here")

msg['Subject'] = "An Email Alert"
msg['From'] = "zzl@1noc.cn"
msg['To'] = "zhangzmg@outlook.com"

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()