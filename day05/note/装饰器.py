#!/usr/bin/evn python
#coding:utf-8

def outer(func):
    def wrapper(arg):
        print 'before'
        func(arg)
        print 'After'
    return wrapper
@outer    
def SayHi(arg):
    print 'Hi',arg

SayHi('nimei')