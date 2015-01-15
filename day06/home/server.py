#!/usr/bin/evn python
#coding:utf-8

import os
import SocketServer
from backend.sqlhelp import *
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
        a=Userinfo()
        des_path= "/tmp/"
        recv_size =0
        print 'Go a conn from :',self.client_address

        data =self.request.recv(1024).split(' ')
        username = data[0]
        passwd = a.GetId(username)
        
        print makemd5(data[1])
        if makemd5(data[1]) != passwd['password']:
            print username 
            data = 'Login Failed!'
            self.request.send(data)
        else:
            pre_data = self.request.recv(1024)
            cmd,file_name,file_size = self.request.recv(1024).split('|')
            recv_size = 0
            #上传文件路径拼接
            file_dir = os.path.join(des_path,file_name)
            f = file(file_dir,'wb')
            Flag = True
            while Flag:
                #未上传完毕，
                if int(file_size)>recv_size:
                    #最多接收1024，可能接收的小于1024
                    data = self.request.recv(1024) 
                    recv_size+=len(data)
                #上传完毕，则退出循环
                else:
                    recv_size = 0
                    Flag = False
                #写入文件
                f.write(data)
            print 'upload successed.'
            f.close()


        
    
ip=('127.0.0.1',9001)
sock = SocketServer.ThreadingTCPServer(ip,MyServer)
sock.serve_forever()
