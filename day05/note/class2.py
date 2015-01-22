#!/usr/bin/evn python
#coding:utf-8

class Func:
    def func1(self):
        print 'Func'

class Bar:
    def func1(self):
        print 'Bar'
#多继承方法相同，继承第一个
class Son(Func,Bar):
    pass

son=Son()
son.func1()
    
    