#!/user/bin/env python
#coding:utf-8
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('localhost',22,'root','.')
stdin,stdout,stderr = ssh.exec_command('cd /tmp;touch 123')
print stdin
ssh.close()
