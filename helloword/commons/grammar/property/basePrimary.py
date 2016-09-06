#!/usr/bin/python
#-*-coding:utf-8-*-
"""
    author: chier
    content: 初次使用 requests类库包，请求一个链接，获取链接的编码格式和内容
    学习资料： http://blog.163.com/yang_jianli/blog/static/161990006201382241223156/

"""
import sys
import inspect

def foo():
    pass # 函数，foo指向这个函数对象

class Cat(object): # 类，Cat指向这个类对象
    def __init__(self, name='kitty'):
        self.name = name
    def sayHi(self): #  实例方法，sayHi指向这个方法对象，使用类或实例.sayHi访问
        print self.name, 'says Hi!' # 访问名为name的字段，使用实例.name访问

cat = Cat() # cat是Cat类的实例对象
print Cat.sayHi # 使用类名访问实例方法时，方法是未绑定的(unbound)
print cat.sayHi # 使用实例访问实例方法时，方法是绑定的(bound)



