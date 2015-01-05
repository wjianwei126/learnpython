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
            return True
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
    
    
class admin(object):
    def __init__(self):
        self.__helper = MysqlHelper()
    def GetSingle(self,param):
        sql = "select * from admin where Name=%s"
        para = (param,)
        return self.__helper.GetSingle(sql,para)
    
    def GetId(self,username):
        sql = "select id from userinfo where username= %s"
        para = (username,)
        return self.__helper.GetId(sql,para)
    
    def AddUser(self,username,password):
        #print username,password
        id = self.GetSingle(username)
        
        #sql = "INSERT INTO userinfo(username,password) VALUES (%s,%s)"
        #INSERT INTO `web`.`userinfo` (`id`, `username`, `password`) VALUES ('3', 'abc', 'abc');
        #para = (param,password,)
        #return self.__helper.AddUser(sql, para)
    
    
if __name__=="__main__":
    username = raw_input("Please input usrname:")
    password=raw_input("Please input password:")
    a = admin()
    #print a.GetSingle('admin')
    #print a.AddUser(username,password)
    print a.GetId(username)
    
