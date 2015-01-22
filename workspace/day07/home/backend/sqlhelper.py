#!/usr/bin/evn python
#coding:utf-8

import MySQLdb
import md5

def makemd5(value):
    hash = md5.new()
    hash.update(value)
    return hash.hexdigest()


class MySqlHelper(object):
    
    def __init__(self):
        self.__connDict = {'host':'192.168.58.128','user':'dbuser','passwd':'0110','db':'web'} 
        
    def __Conn(self):
        try:
            conn = MySQLdb.connect(**self.__connDict)
        except Exception,e:
            data = 'can not connect!'
            conn = data
        return conn
    def GetSingle(self,sql,paramters):
        conn = self.__Conn()
        if not conn:
            print 'can not connect!'
            return None
        try:
            cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            cur.execute(sql,paramters)
            data = cur.fetchone()
            print data
        except Exception,e:
            data =None
            print 'can not connect!'
            
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
            data = cur.fetchone()
            print data 
            return data
        except Exception,e:
            data =None
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
    
    def AddHost(self,sql,paramters):
        conn = self.__Conn()
        cursor = conn.cursor()
        try:
            cursor.execute(sql,paramters)
            data = conn.commit()
            id=cursor.lastrowid
            return id
        except:
            print 'add host failed!'
            conn.rollback()

    def GetHost(self,sql,paramters):
        conn = self.__Conn()
        cursor = conn.cursor()
        try:
            cursor.execute(sql,paramters)
            data = cursor.fetchone()
            return data 
        except:
            return False
        
    def UpdateMsg(self,sql,paramters):
        conn = self.__Conn()
        cursor = conn.cursor()
        try:
            cursor.execute(sql,paramters)
            data = conn.commit()
        except:
            print 'error'

    def GetMid(self,sql,paramters):
        conn = self.Conn()
        cursor = conn.curson()
        try:
            cursor.execute(sql,paramters)
            data = cursor.fetchone()
            return data
        except:
            print 'error'
