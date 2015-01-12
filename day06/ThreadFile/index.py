#!/usr/bin/evn python
#coding:utf-8

import threading
import time
#from test.test_threading_local import target
'''
def call(arg):
    for i in range(100):
        print i
        time.sleep(1)


t1=threading.Thread(target=call,args=('nidaye',))
print  t1.isDaemon()
t1.setDaemon(True)
t1.start()

print '------------end'
#print t1.isAlive()
'''


def Func1(arg):
    print 'Func1'
    time.sleep(6)
    print 'Func-end'
def Func2(arg):
    print 'Function2'
    time.sleep(2)
    print 'Func2-end'
    
t1= threading.Thread(target=Func1,args=('func1',))
t1.setDaemon(True)
t1.start()


t2 = threading.Thread(target= Func2,args=('Func2',))
t2.start()

print 'end\n'





