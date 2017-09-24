#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Filename: demo2
# @Date    : 2017-09-24 11:56
# @Author  : zzl
#from   http://blog.csdn.net/cellurs/article/details/69367635s
"""
   python_version  3.4
"""
import time,os,traceback,random
import requests,re
from bs4 import BeautifulSoup

#define
Agent =['Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1'
        ,'Opera/9.27 (Windows NT 5.2; U; zh-cn)'
        ,'Mozilla/5.0 (iPhone; U; CPU like Mac OS X) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0'
        ]
def ProcName(name):#清洗目录名
    pat = r'[<|>|/|\|||:|"|*|?]+|（提示：已启用缓存技术，最新章节可能会延时显示，登录书架即可实时查看。）'
    pat = re.compile(pat)
    return pat.sub('',name)

def log(url):
    path = "\home\Rullec\log.txt"
    with open(path,'w') as f:
        f.write(str(url))
        f.close()

def GetHtmlText(url):#获得HTML页面内容 此处可以增加proxies代理服务器，只不过目前还没有
    try:
        r = requests.get(url,headers={'User-Agent':Agent[random.randint(0,Agent.__len__()-1)]},timeout = 20)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except requests.exceptions.ReadTimeout|requests.exceptions.ConnectTimeout:
        traceback.print_exc() #如果出现超时错误
        #log(url)
        waittime = random.randint(10, 20)
        print("出现超时错误！等待"+str(waittime)+"秒!\n")
        time.sleep(waittime)
        return None

def FindIndex(name):#获得目标小说目录页
    url = "http://zhannei.baidu.com/cse/search?&s=287293036948159515&q="+str(name)+"&click="+str(random.randint(1,3))+'&nsid='
    text = GetHtmlText(url)
    if text==None:
        print("文本为空，无法解析")
        return None
    soup = BeautifulSoup(text.encode('utf-8'),'html.parser')
    list = soup.find_all(name = 'a',attrs = {"cpos" :"title","title":name})#一个list
    url = []
    for i in list:
        url.append(i["href"])
    return url

def ProcTxt(text):
    text = text[9:]
    pat = r'    '
    pat = re.compile(pat)
    return pat.sub("\n",text)

def Write(storpath,tag):#进行小说的存储
    if None==tag:
        print('小说写入失败，原因是小说最后一层超链接无法获取')
        return 1
    a = tag.a#标签的属性使用tag['title']来获得，标签下的搜索使用tag.children来实现
    storpath += "/"+ProcName(a.string)+".txt"
    while os.path.exists(storpath):
        if time.time()-os.path.getctime(storpath)<100 :
            newpath = storpath.split('.')
            storpath = newpath[0] + "#.txt"
        else:
            return 1
    url = 'http://www.biquge.com/'+a['href']
    text = GetHtmlText(url)
    if text==None or len(text)==0:
        print("最后一层文本获取失败!")
        return 1
    soup = BeautifulSoup(text.encode('utf-8'),'html5lib')
    novel = soup.find_all("div",attrs={"id":"content"})
    text = novel[0].text
    #开始写入
    with open(storpath,'w',encoding='utf-8') as f:
        text = ProcTxt(str(text))
        f.write(text)
        f.close()
    return 0

def Spider(url,path):#爬取小说目录页
    text = ""
    #while len(text) or text==None:
    text = GetHtmlText(url)
    num = 0
    soup = BeautifulSoup(text,'html5lib')
    list = soup.find_all(["dd","dt"])
    nowpath = ""
    flag = 0
    for i in list:
        if i.name == "dt":
            nowpath = path+"/"+ProcName(i.string)
            if os.path.exists(nowpath):
                pass
            else:
                os.mkdir(nowpath)
        else:
            flag = Write(nowpath,i)
            num+=1
            if num%10==0 and (not flag):
                time.sleep(random.randint(3,10))#爬虫每爬几个就休眠
        print("\r当前进度: {:.2f}%".format(num * 100 / len(list)), end="")
    return ""

def main():#主函数
    name = ProcName(input("请输入要爬取的小说的名字:"))
    url = FindIndex(name)#爬取搜索结果，在其中查找目录页，并且返回
    if 0==len(url):
        print("查无此小说")
        exit()
    path = "E:\小说\\"
    #path = "\home\Rullec\小说\\"
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    path = path +name
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    Spider(url[0],path)
main()


