#!/usr/bin/python
#-*-coding:utf-8-*-

'''
Created on 2015-1-16
初学PYTHON，用于抓取美女图片；
python version: python34
业务逻辑：
    


参考资料：
    http://my.oschina.net/lj2007331/blog/144784 Python通过代理多线程抓取图片
    http://www.169it.com/article/7983909274263214058.html Python3通过request.urlopen实现Web网页图片下载

@author: zhangzhanliang
'''
import request
from  datetime  import  *  
import threading
from time import sleep, ctime
from html import parser

def downjpg(filepath, FileName="default.jpg"):
    try:
        FileName = getFileName(filepath)
        web = request.urlopen(filepath)
        print("访问网络文件" + filepath + "\n")
        jpg = web.read()
        DstDir = "G:\\happy_python\\"
        print("保存文件" + DstDir + FileName + "\n")
        try:
            File = open(DstDir + FileName, "wb")
            File.write(jpg)
            File.close()
            return
        except IOError:
            print("error\n")
            return
    except Exception:
        print("error\n")
        return
    
'''
   根据URL路径，返回文件名
'''
def getFileName(fileUrl):
    file_name = str(fileUrl).split("/")[-1]
    file_name = str(date.today()) + "-" +file_name
    return file_name

def downjpgmutithread(filepathlist):
    print("共有%d个文件需要下载" % len(filepathlist))
    for file in filepathlist:
        print(file)
    print("开始多线程下载")
    task_threads = []  # 存储线程
    count = 1
    for file in filepathlist:
        t = threading.Thread(target=downjpg, args=(file, "%d.jpg" % count))
        count = count + 1
        task_threads.append(t)
    for task in task_threads:
        task.start()
    for task in task_threads:
        task.join()  # 等待所有线程结束
    print("线程结束")
'解析 HTML 信息，获取URL路径和相关的信息，存储到对象中，然后通过线程调用下载'
class parserLinks(parser.HTMLParser):
    filelist = []
    def handle_starttag(self, tag, attrs):
        print("============ start")
        print(tag)
        print(attrs)
        print("============ end ")
        if tag == 'img':
            for name, value in attrs:
                if name == 'src':
                    print(value)
                    self.filelist.append(value)
                    # print( self.get_starttag_text() )
    def getfilelist(self):
        return self.filelist

def main(WebUrl):
    # globals flist
    if __name__ == "__main__":
        lparser = parserLinks()
        web = request.urlopen(WebUrl)
        # context= web.read()
        for context in web.readlines():
            _str = "%s" % context
            try:
                lparser.feed(_str)
            except parser.HTMLParseError:
                # print( "parser error")
                pass
        web.close()
        imagelist = lparser.getfilelist()
        downjpgmutithread(imagelist)      
        # downjpgmutithread( flist)
# WebUrl="http://www.baidu.com/" #要抓去的网页链接,默认保存到e盘
WebUrl = "http://sexy.faceks.com/post/2c9c66_14c4e92"
main(WebUrl)


