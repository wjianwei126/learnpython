#/usr/bin/env python
#coding:utf-8

import paramiko

def ssh_client(ser_group,ser_cmd):
    private_file_path = '/root/.ssh/id_rsa'
    key = paramiko.RSAKey.from_private_key_file(private_file_path)

    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ser_group,username='mingming',port=22,pkey=key)
    stding,stdout,stderr= ssh.exec_command(ser_cmd)
    sshclose()


