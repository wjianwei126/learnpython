#!/usr/bin/evn python
#coding:utf-8

import SocketServer
from SocketServer import BaseRequestHandler

class MyServer(SocketServer.BaseRequestHandler):
    
    def handle(self):
        print self.request
        print self.client_address
        
    
ip=('127.0.0.1',9000)
sock = SocketServer.ThreadingTCPServer(ip,MyServer)
sock.serve_forever()
