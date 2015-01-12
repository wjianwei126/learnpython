#!/usr/bin/evn python
#coding:utf-8

import threading
from Queue import Queue
import time

queue =Queue()

def Create(i):
    while True:
        if queue.qsize()< 100:
            print i,'生产的包子\n'
            queue.put(str(i)+'de 包子')
        else:
            time.sleep(20)

def Producer():
    list =  ['aaa','bbbb','cccc']
    for i in list:
        t = threading.Thread(target=Create,args=(i,))
        t.start()

def consumer():
    while True:
        baozi = queue.get()
        print baozi
        print queue.qsize()
        time.sleep(1)
        
Producer()
consumer()