#!/usr/bin/evn python
#coding:utf-8

import socket

ip = ('127.0.0.1',9000)
sk = socket.socket()
sk.connect(ip)


#while True:
    # = sk.recv(1024)
    # data
    #if data == 'close':
#break
    #inp = raw_input("Input:")
    #sk.sendall(input)
sk.close()
