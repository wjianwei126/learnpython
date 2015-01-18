#!/user/bin/env python
#coding:utf-8

#多进程
'''
from multiprocessing import Process
import time
from multiprocessing import Array
    

array = Array('i',[0,0,0,0])
#Array多进程共享数据
#li=[]不能共享数据
def Foo(i):
    array[i] = 1000+i
    for item in array:
        print i,'---->',item
#    li.append(i)
#    print li
#    time.sleep(5)

for i in range(4):
    p= Process(target=Foo,args=(i,))
    p.start()
    p.join()
#IO密集使用多线程，不占用CPU
#计算密集，使用多进程
'''
'''
from multiprocessing import Process
from multiprocessing import Manager
manager = Manager()
dic = manager.dict()
l = manager.list()

def Foo(i):
    dic[i] = 1000+i
    print dic
for i in range(4):
    p= Process(target=Foo,args=(i,))
    p.start()
    p.join()
'''


#进程池
from multiprocessing import Process,Pool
def Foo():
    return 'nimei'

def Bar(arg):
    print arg
    print 'god'
    

pool = Pool(10)
#re = pool.apply(Foo)
#print re
pool.apply_async(func=Foo,callback=Bar).get()
#apply_async 回调函数

