#!/usr/bin/evn python
#coding:utf-8

import MySQLdb


class MysqlHelper(object):
    
    def __init__(self):
        self.__Host = 'kali'
        self.__User = 'dbuser'
        self.__Passwd = '0110'
        self.__DB = 'web'
        
    def __Conn(self):
        try:
            conn = MySQLdb.connect(host=self.__Host,user=self.__User,passwd=self.__Passwd,db=self.__DB)
        except Exception,e:
            data = 'can not connect!'
            conn = data
        return conn
    def GetSingle(self,sql,paramters):
        conn = self.__Conn()
        if not conn:
            return None
        try:
            cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            cur.execute(sql,paramters)
            #cur.execute("select Name,Nickname from admin where Name=%s",(admin,))
            data = cur.fetchone()
            print data
        except Exception,e:
            data =None
            #写个日志
        finally:
            cur.close()
            conn.close()
        return data
    def GetId (self,sql,paramters):
        conn = self.__Conn()
        if not conn:
            return None
        try:
            cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            cur.execute(sql,paramters)
            #cur.execute("select Name,Nickname from admin where Name=%s",(admin,))
            data = cur.fetchone()
            return data
        except Exception,e:
            data =None
            #写个日志
        finally:
            cur.close()
            conn.close()
        return data
    
    def AddUser(self,sql,paramters):
        conn = self.__Conn()
        cursor = conn.cursor()
        #print sql,paramters
        try:
            cursor.execute(sql,paramters)
            data = conn.commit()
            id=cursor.lastrowid
            return id
        except:
            print 'error'
            conn.rollback()
    
    def AddMsg(self,sql,paramters):
        conn = self.__Conn()
        cursor = conn.cursor()
        try:
            cursor.execute(sql,paramters)
            data = conn.commit()
            id=cursor.lastrowid
            return id
        except:
            print 'error'
            conn.rollback()
            
    def UpdateMsg(self,sql,paramters):
        conn = self.__Conn()
        cursor = conn.cursor()
        try:
            cursor.execute(sql,paramters)
            data = conn.commit()
        except:
            print 'error'
    
class Admin(object):
    def __init__(self):
        self.__helper = MysqlHelper()
        
    def GetSingle(self,param):
        sql = "select * from admin where Name=%s"
        para = (param,)
        return self.__helper.GetSingle(sql,para)
 
 
class Userinfo:
    def __init__(self):
        self.__helper = MysqlHelper()
           
    def GetId(self,username):
        sql = "select id,password from userinfo where username= %s"
        para = (username,)
        return self.__helper.GetId(sql,para)
    
    def AddUser(self,username,email,password):
        #print username,password
        sql = "INSERT INTO userinfo(username,email,password) VALUES (%s,%s,%s)"
        para = (username,email,password,)
        return self.__helper.AddUser(sql, para)

    def DelUser(self,username):
        #print username,password
        sql = "delete from userinfo where username= %s"
        para = (username,)
        return self.__helper.DelUser(sql, para)

class Msg:
    def __init__(self):
        self.__helper = MysqlHelper()
    def AddMsg(self,mid,username,msg):
        sql = "INSERT INTO msg(Mid,Username,Message) VALUES (%s,%s,%s)"
        para = (mid,username,msg,)
        return self.__helper.AddMsg(sql, para)

    def UpdateMsg(self,mid,msg):
        sql = "INSERT INTO msg(Mid,Username,Message) VALUES (%s,%s,%s)"
        para = (mid,msg,)
        return self.__helper.AddMsg(sql, para)


 
