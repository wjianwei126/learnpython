#!/usr/bin/evn python
#coding:utf-8


import MySQLdb
'''
# 打开数据库连接
db = MySQLdb.connect("kali","dbuser","0110","web" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("select * from admin")

# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchall()

print data

cursor.close()
# 关闭数据库连接
db.close()
'''
'''
conn = MySQLdb.connect(host='kali',user='dbuser',passwd='0110',db='web')
#MySQLdb.connections.Connection

cur = conn.cursor()
#MySQLdb.cursors.Cursor

#li = ['nimei','Japan']
#cur.execute('insert into admin(Name,NickName) \
#    values(%s,%s)',li)
li = [('admin','Ch'),
      ('admin2','Ch'),
      ('admin3','Ch')]
#execute 返回受影响的条数executemany(self, query, args):
a = cur.executemany("insert into admin(Name,NickName)\
                values(%s,%s)",li)
conn.commit()
cur.close()
conn.close()
print a 
'''
'''
conn = MySQLdb.connect(host='kali',user='dbuser',passwd='0110',db='web')

cur = conn.cursor()
#a= cur.execute("delete from admin where Name='admin3'")
#b = cur.execute("truncate table admin")
c = cur.execute("update admin set name = %s",['aaa'])
conn.commit()
print c
cur.close()
conn.close()

'''
conn = MySQLdb.connect(host='kali',user='dbuser',passwd='0110',db='web')
#cur=conn.cursor()
#data 字典类型输出
cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
nRet= cur.execute('select * from admin')
print nRet
data = cur.fetchall()
#print cur.fetchone()
#print cur.fetchone()
#scroll 
cur.scroll(0,'absolute')

#print cur.fetchone()
#print cur.fetchone()

cur.close()
conn.close()

#print data
for item in data:
    print item

'''
conn = MySQLdb.connect('kali','dbuser','0110','web')

cur = conn.cursor()


li = [('ad','Ch'),
      ('ad2','Ch'),
      ('ad3','Ch')]
#execute 返回受影响的条数executemany(self, query, args):
a = cur.executemany("insert into admin(Name,NickName)\
                values(%s,%s)",li)

conn.commit()
print cur.lastrowid

cur.close()
conn.close()
'''