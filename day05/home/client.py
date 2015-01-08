#!/usr/bin/evn python
#coding:utf-8

import socket

ip = ('127.0.0.1',9004)
client = socket.socket()
client.connect(ip)

def input(data):
    while True: 
        username =raw_input('Please replace input username:')
        client.sendall(username)
        password =raw_input('please input password:')
        client.sendall(password)
        data = client.recv(1024)
        if data == 'login':
            break
    return True




def client_connect():
    
    
    while True:
        data = client.recv(1024)
        print data
        inp = raw_input(':').strip()
        if not data or data == 'exit':
            break
        client.sendall(inp)
    client.close()

username =raw_input('Please input username:')
client.sendall(username)
password =raw_input('please input password:')
client.sendall(password)
data = client.recv(1024)
print data
if data != 'login':
    if input(data):
        client_connect()
else:
    client_connect()
