#!/usr/bin/evn python
#coding:utf-8

import socket
from sqlhelp import *



#while True:

sk = socket.socket()
ip_port = ('127.0.0.1',9005)
sk.bind(ip_port)
sk.listen(5)



def login(u,p):
    conn,addr = sk.accept()
    a = Userinfo()
    user = a.GetId(u)
    print user
    if user == None:
        data ='Faild'
        conn.sendall(data)
        return data
    else:
        if p != user['password']:
            data= 'Password is Wrong!'
            conn.sendall(data)
            return False
        else:
            return True
   

def connect():   
    flag = True
    conn,addr = sk.accept()
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



def accept():
    flag = True
    while flag:
        conn,addr = sk.accept()
        username = conn.recv(1024)
        password = conn.recv(1024)
        print login(username,password)
#        if login(username, password)== True:
#            flag == False
    return True
accept()

'''

if login(username,password):
    connect()
else:
    print "Login Failed retry please."
'''
