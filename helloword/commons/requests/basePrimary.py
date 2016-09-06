#!/usr/bin/python
#-*-coding:utf-8-*-
"""
    author: chier
    content: 初次使用 requests类库包，请求一个链接，获取链接的编码格式和内容
        官方网址：http://www.python-requests.org/en/master/
            http://cn.python-requests.org/zh_CN/latest/
"""
#coding=utf-8
import requests
def main():
    r = requests.get('http://www.zhidaow.com')
    print r.encoding
    print r.content
    print r.text


if __name__ =='__main__':
    main()