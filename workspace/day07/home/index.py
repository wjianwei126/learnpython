#!/user/bin/env python
#coding:utf-8
import paramiko
import os
from multiprocessing import Process,Pool
from backend.models import *
         

class multissh:
    
    def __init__(self):
        self.a=hosts()
   #     self.__process = None
        self.__ssh = paramiko.SSHClient()
        self.__ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def start(self,host,cmd):
        self.__host= host
        self.__process = Process(target=self.__run(host,cmd))
        self.__process.start()

    def run(self,gid,cmd):
        self.__b = self.a.GetHost(gid)
        print self.__b
        self.__ssh.connect(self.__b[2],int(self.__b[4]),self.__b[5],self.__b[6])
        stdin,stdout,stderr = self.__ssh.exec_command(cmd)
        print stdout.read()
        self.__ssh.close()
    


if __name__=="__main__":
    abc = multissh()
    while True:
        gid = raw_input('please input gid:')    #输入默认组101
        if gid:
            cmd = raw_input('input shell cmd:') #输入shell命令
            abc.run(gid,cmd) 
        if gid == 'exit':
            os.exit('exit')
