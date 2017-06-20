#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Filename: 4-mysqlBasicExample
# @Date    : 2017-06-20 14:19
# @Author  : zzl
"""
   python_version  2.7.11
"""

import pymysql
conn = pymysql.connect(host='127.0.0.1',
                       port=3356,
                       user='root',
                       passwd="secret",
                       db='mysql')
cur = conn.cursor()
cur.execute("USE scraping")
cur.execute("SELECT * FROM pages WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close()


