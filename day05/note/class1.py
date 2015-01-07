#!/usr/bin/evn python
#coding:utf-8

class Msg:
    def __init__(self):
        self.Url = 'www.baidu.com'
    def Send(self,phone):
        print '发送成功'
    def SendMulti(self,phone):
        print '群发'
        
class Email:
    def __init__(self):
        self.url= 'www.'
    def Send(self,email):
        print '发送成功'
    def SendMulti(self,email):
        print 'dfadf'
#sender =Msg()
def ResetPwd(obj):
#sender.Send()
    print '修改成功' 
    obj.Send('22')  
        
sel = raw_input("input:")
if sel == 1:
    #send实例化类对象
    sender =Msg() 
else:
    sender =Email()

#把类对象传递给ResetPwd函数
ResetPwd(sender) 

#self 实例化对象，self就是对象本身

