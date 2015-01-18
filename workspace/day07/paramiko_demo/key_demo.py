#/usr/bin/env python
#coding:utf-8

import paramiko

private_file_path = '/root/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(private_file_path)

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='localhost',username='mingming',port=22,pkey=key)
stding,stdout,stderr= ssh.exec_command('touch ~/nimei')
ssh.close()


