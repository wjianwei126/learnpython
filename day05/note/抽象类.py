#!/usr/bin/evn python
#coding:utf-8
from abc import ABCMeta, abstractmethod
#抽象类抽象方法
#约束子类使用Send方法
class Interface:
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def Send(self):
        pass

class Foo(Interface):
    def SayHi(self):
        pass
    def Send(self):
        print 'send'
        
f = Foo()
f.Send()