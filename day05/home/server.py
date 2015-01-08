#!/usr/bin/evn python
#coding:utf-8

import socket
from sqlhelp import *


#while True:

sk = socket.socket()
ip_port = ('127.0.0.1',9001)
sk.bind(ip_port)
sk.listen(5)
conn,addr = sk.accept()


def login(u,p):
    a = Userinfo()
    user = a.GetId(u)
    id  = user['id']
    if user != None:
        if makemd5(p) == user['password']:
            conn.sendall('1')
            return id
        else:
            data= 'Password is Wrong!'
            conn.sendall(data)
            return False
    else:
        data = "The user is not exsit!"
        conn.sendall(data)
        return False
    return id 

def connect(oid):   
    b = Msg()
    v = b.Getid(oid)
    
        
    flag = True
    conn.sendall('Hello,what can I do for you?')
    while flag:   
        data =conn.recv(1024)
        print data
        if v == None:
            b.AddMsg(oid, data)
        else:
            b.UpdateMsg(mid,oid,data)
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
        id = login(username, password)
        if id != None:
            print "Login success"
            break
    return id
    
id = auth()
if id != None:
    connect(id)
