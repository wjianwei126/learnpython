#!/usr/bin/evn python
#coding:utf-8

import SocketServer
from SocketServer import BaseRequestHandler

class MyServer(SocketServer.BaseRequestHandler):
    
    def handle(self):
        print self.request
        print self.client_address
        print self.request.recv(1024).strip()
        
    
ip=('127.0.0.1',9001)
sock = SocketServer.ThreadingTCPServer(ip,MyServer)
sock.serve_forever()