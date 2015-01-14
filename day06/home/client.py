#!/usr/bin/evn python
#coding:utf-8

import socket
import os

skk=socket.socket()
serveraddress = raw_input('Please input ServerAddress:').strip()
ip_port = (serveraddress,9000)
skk.connect(ip_port)


container= {'key':'','data':''}
username = raw_input("Please input username:").strip()
password = raw_input('Please input password:')
skk.send(username+' '+password)
data = skk.recv(1024)
if data!= False:
    while True:
        inp = raw_input('Input:').strip()   
        cmd,path = input.split('|')
        file_name = os.path.basename(path)
        file_size= os.stat(path).st_size
        skk.send(cmd+'|'+file_name+'|'+str(file_size))
        send_size =0
        f = file(path,'rb')
        Flag =True
        while Flag:
            if send_size + 1024 > file_size:
                data=f.read(file_size-send_size)
                Flag = False
            else:
                data = f.read(1024)
                send_size+=1024
            skk.send(data)
        f.close() 