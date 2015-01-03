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
            conn = MySQLdb.connect(host=self.__Host,user=self.__User,passed=self.__Passwd,db=self.__DB)
        except Exception,e:
            conn = None
        return conn
    
    def GetSingle(self,sql,paramters):
        conn = self.__Conn()
        if not conn:
            return None
        try:
            cur = conn.cursor(cursorclass =MySQLdb.cursors.DictCursor)
            cur.execute(sql,paramters)
            data = cur.fetchone()
        except Exception,e:
            data =None
            #写个日志
        finally:
            cur.close()
            conn.close()
        return data
    
class admin(object):
    def __init__(self):
        self.__helper = MysqlHelper()
    def GetSingle(self,param):
        sql = "select Name,Nickname from admin where Name=%s"
        para = (param,)
        return self.__helper.GetSingle(sql,para)
    
if __name__=="__main__":
    a = admin()
    print a.GetSingle('admin')