#!/usr/bin/env python
#coding:utf-8

from sqlhelp import *




do = raw_input('ADD,DEL,UPDATE,CHECK\nWhat do you want to do ?')


if do == 'ADD':
    username = raw_input('please user name:')
    password = raw_input('please input password:')
    a = Userinfo()
    passwd =makemd5(password)
    print a.AddUser(username, passwd)
    
#username = raw_input("Please input usrname:")
'''
if  a.GetId(username) == None:
    email= raw_input('Please input email address:')
    password=raw_input("Please input password:")
    print a.AddUser(username,email,password)
else:
    print "Username is exsit!"
''' 

        
        

