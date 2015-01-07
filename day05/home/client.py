#!/usr/bin/evn python
#coding:utf-8

import socket

ip = ('127.0.0.1',9001)
client = socket.socket()
client.connect(ip)

username =raw_input('Please input username:')
client.sendall(username)
password =raw_input('please input password:')
client.sendall(password)
while True:
    data = client.recv(1024)
    print data
    inp = raw_input(':').strip()
    if not data or data == 'exit':
        break
    client.sendall(inp)
client.close()
