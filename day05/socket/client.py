#!/usr/bin/evn python
#coding:utf-8

import socket

ip = ('127.0.0.1',9010)
sk = socket.socket()
sk.connect(ip)

while True:
    data = sk.recv(1024)
    print data
    if data == 'close':
        break
    inp = raw_input("Input:")
    sk.sendall(input)
sk.close()
