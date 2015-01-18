#!/user/bin/env python
#coding:utf-8
import paramiko

def ssh_ser(ser_host,ser_cmd):
    paramiko.util.log_to_file('/tmp/redmine.log')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ser_host,22,'root','kevinstar')
    stdin,stdout,stderr = ssh.exec_command(ser_cmd)
    print stdout.read()
    ssh.close()

def ssh_put():
    sftp = paramiko.Transport(('ip',22))

def first_conn():
    cmd_base=('echo VM06 > /etc/hostname','apt-get -y update && apt-get dist-upgrade','apt-get -y install ntp')
    for cmd in cmd_base:
        ssh_ser('192.168.1.91',cmd)

def inst_redmine(cmd_poll):
    for cmd in cmd_poll:
        ssh_ser('192.168.1.91',cmd.strip())
        #print cmd.strip()
