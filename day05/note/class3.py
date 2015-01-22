#!/usr/bin/evn python
#coding:utf-8
class Foo:
    def __init__(self):
        print 'Foo.__int__'
    def __call__(self):
        print 'Foo.__call__'

f = Foo()
# f() = f.__call__()
f()