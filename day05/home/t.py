#!/usr/bin/evn python
#coding:utf-8

import socket
#from server import *
from sqlhelp import *







a = Userinfo()
sk = socket.socket()
ip_port = ('127.0.0.1',9999)
sk.bind(ip_port)
sk.listen(5)
conn,addr = sk.accept()

#print login('admin', 'admin')