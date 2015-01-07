#!/usr/bin/evn python
#coding:utf-8

import SocketServer
from SocketServer import BaseRequestHandler


class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        print self.client_address
        username = self.request.recv(1024).strip()
        password = self.request.recv(1024).strip()
        userinfo = [username,password]
        #if len(username) > 0:
        return userinfo
'''        
        print password
            self.request.send('What can I do for you?')
            while True:
                data= self.request.recv(1024).strip()
                if not data:
                    break
                print data
                inp = raw_input(":")
                self.request.send(inp)

        else:
            data = 'close'
            self.request.sendall(data)

'''

    
