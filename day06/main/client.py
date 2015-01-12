#!/usr/bin/evn python
#coding:utf-8

import socket
import os

skk  = socket.socket()
ip_port = ('127.0.0.1',9000)
skk.connect(ip_port)


while True:
    inp = raw_input('Input:').strip()
    if inp.startswith('put'):
        filename = inp.split()[1]
        print filename
        f= file(filename,'rb')
        f_size = os.stat(filename).st_size
        
        only_filename = filename.split('\\')[-1]
        msg = '%s#%s#%s' % ('put',only_filename,f_size)
        print msg
        skk.sendall(msg)
        skk.sendall(f.read())
        f.close()
        res= skk.recv(1024)
        print res
'''
while True:
    data = skk.recv(1024)
    print data
    
    if data == 'close':
        break
    
    inp = raw_input('Input:')
    f=file(inp,'rb')
    data = f.read()
    f.close()
    skk.sendall(data)
    
skk.close()
'''