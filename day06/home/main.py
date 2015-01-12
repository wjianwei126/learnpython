#!/usr/bin/evn python
#coding:utf-8

import SocketServer
#import cmd
#from SocketServer import BaseRequestHandler

class MyServer(SocketServer.BaseRequestHandler):
   
    def recv_all(self,f_obj,total_size):
        while total_size !=0:
            if total_size <4096:
                data = self.request.recv(total_size)
                total_size = 0
            else:
                data = self.request.recv(4096)
                total_size -=4096
            f_obj.write(data)
        return True
   
    def handle(self):
        print 'Go a conn from :',self.client_address
        while True:
            cmd =self.request.recv(1024)
            option,filename,size = cmd.split('#')
            print '-->',option,filename,size
            f = file('../files/%s' % filename, 'wb')
            res = self.recv_all(f,int(size))
            if res is True:
                f.close()
                self.request.send('File: %s has upload success'% filename)
    
    
ip=('127.0.0.1',9000)
sock = SocketServer.ThreadingTCPServer(ip,MyServer)
sock.serve_forever()