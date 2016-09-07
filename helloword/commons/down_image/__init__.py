#!/usr/bin/python
#-*-coding:utf-8-*-

from  datetime  import  *

def __init__():
    url="abaie.ipg"
    name = url.split('.')[0]     #获取图片后缀
    pic_suffix = url.split('.')[-1]  #获取图片后缀
    print(name)
    print(pic_suffix)
    
    
    url1 = "http://imglf1.ph.126.net/-UO433jEITTNHHJrus64Jw==/6608269392097510543.jpg"
    name1 = url1.split("/")[-1]
    suffix1 = url1.split("/")[-1]
    print(name1)
    print(suffix1)
    
    file_name = "zhang"
    file_name = str(date.today())+'-' + file_name
    
    print('date.today():' , date.today())
    print(file_name)
__init__()