#!/usr/bin/env python
#coding:utf-8

from sqlhelper import MySqlHelper

class UserInfo:
    
    def __init__(self):
        self.sqlHelper = MySqlHelper()
    
    def CheckLogin(self,name,pwd):
        '''验证用户名是否合法
        @param name:用户名
        @param pwd:密码
        @return: 如果登录成功，返回该用户的自增ID；否则，返回False 
        '''
        sql = '''select Nid,Name,Password from UserInfo where Name=%s and Password = %s'''
        params = (name,pwd,)
        result = self.sqlHelper.GetSimple(sql, params)
        if not result:
            return False
        else:
            return result['Nid']
    
class ChatRecord:
    
    def __init__(self):
        self.sqlHelper = MySqlHelper()
        
    def InsertRecord(self,message,date,userid):
        '''插入聊天记录
        @param message:聊天信息
        @param date:时间
        @param userid:用户ID
        @return: 如果聊天记录插入成功，返回True；否则返回False 
        '''
        sql = '''insert into ChatRecord(Message,Date,UserId) values(%s,%s,%s)'''
        params = (message,date,userid,)
        result = self.sqlHelper.InsSample(sql, params) #插入聊天记录，返回受影响条数，如果受影响条数为 1，表示插入成功
        if result != 1:
            return False
        else:
            return True
            
    def GetRecord(self,userid):
        '''获取聊天记录
        @param userid:用户ID
        @return: 所有聊天记录
        '''
        sql = ''' select Message,Date from ChatRecord where UserId=%s '''
        params = (userid,)
        result = self.sqlHelper.GetDict(sql, params)#根据用户ID，获取该用户的所有聊天记录
        print result
        if not result:
            return False
        else:
            return result
        
        
        
        
        