#!/user/bin/env python
#coding:utf-8
import paramiko
class ssh_ser():

    def __init__(self,Host,Username,Passwdi,Cmd):
        self.Host=host
        self.Port=port
        self.Username=username
        self.Passwd=password
        self.Cmd=cmd
         
    def ssh_ser(self):
        paramiko.util.log_to_file('/tmp/redmine.log')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.Host,sefl.Port,self.Username,self.Cmd)
        stdin,stdout,stderr = ssh.exec_command(ser_cmd)
        print stdout.read()
        ssh.close()

    def ssh_put(self):
        sftp = paramiko.Transport((self.Host,self.Port))

    def first_conn(self):
        cmd_base=('echo VM06 > /etc/hostname','apt-get -y update && apt-get dist-upgrade','apt-get -y install ntp')
        for cmd in self.Cmd:
            ssh_ser(self.Port,cmd)

    def inst_redmine(self):
        for cmd in self.Cmd:
            ssh_ser('192.168.1.91',cmd.strip())
            #print cmd.strip()
