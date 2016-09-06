#!/usr/bin/python
#-*-coding:utf-8-*-
"""
    author:chier
    content:使用requests类库包,请求一个链接,返回的内容是JSON格式的数据,对数据进行解析
        官方网址:http://www.python-requests.org/en/master/
            http://cn.python-requests.org/zh_CN/latest/
"""
import requests
def main():
    r = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=122.88.60.28')
    print r.text
    print r.json()['data']['country']



if __name__ =='__main__':
    main()