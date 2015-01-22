#!/usr/bin/evn python
#coding:utf-8
'''
def outer(fun):
    print 'aaaa'
    fun()

def Func1():
    print 'nimei'
    pass

Func1()

outer(Func1)
'''
def outer2(arg):
    def wapper():
        print 'test outer2'
        arg()
    return wapper
    

@outer2
def Func2():
    print 'kengdie'
    pass

Func2()
'''
@outer2 = outer2(Func2) =def wapper():
                                print 'aa'
                                 arg()
                         return wapper
'''

