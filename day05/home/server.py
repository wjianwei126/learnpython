#!/usr/bin/evn python
#coding:utf-8

import socket
from sqlhelp import *



#while True:

sk = socket.socket()
ip_port = ('127.0.0.1',9004)
sk.bind(ip_port)
sk.listen(5)
conn,addr = sk.accept()


def login(u,p):
    a = Userinfo()
    user = a.GetId(u)
    if user == None:
        print "not exsit!"
        data = "Fail"
        conn.sendall(data)
    else:
        if p != user['password']:
            data= 'Password is Wrong!'
            conn.sendall(data)
            return False
        else:
            data = 'login'
            conn.sendall(data)
            return True
   

def connect():   
    flag = True
    conn.sendall('Hello,what can I do for you?')
    while flag:   
        data =conn.recv(1024)
        print data
        if data == 'exit':
            conn.sendall('close')
            flag = False
        else:
            inp = raw_input(':').strip()
            conn.sendall(inp)
        
    conn.close()


def auth():
    while True:
    #    print addr
        username = conn.recv(1024)
        password = conn.recv(1024)
        if login(username, password) == True:
            print "Login success"
            break
    return True
if auth():
    connect()
'''

if login(username,password):
    connect()
else:
    print "Login Failed retry please."
'''
