#!/usr/bin/evn python
#coding:utf-8
import socket


sk = socket.socket()
ip_port = ('127.0.0.1',9010)
sk.bind(ip_port)
sk.listen(5)

while True:
    conn,addr = sk.accept()
    conn.sendall('Welcome...')
    flag = True
    while flag:
        data =conn.recv(1024)
        print data
        if data == 'exit':
            conn.sendall('close')
            flag = False
        else:
            conn.sendall('nimei')
    conn.close()        