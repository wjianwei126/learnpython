#!/usr/bin/env python 
#coding:utf-8

'''
__import__(name, globals={}, locals={}, fromlist=)
getattr(object, name)

#以字符串形式，导入模块，通过字符串执行函数

moudle = __import__('os')
check1 = hasattr(moudle, 'path')
print check1

check2 = getattr(moudle, 'path')
print check2

check3 = delattr(moudle, 'path')
print check3

#生成随机数
import random
print random.randrange(10000,100000)

#数字转换ASSIC码
chr(80)


#生成随机码
import random
temp = ''
for i in range(8):
    rm = random.randrange(0,4)
    if rm != 1:
        temp = temp +  chr(random.randrange(65,90))
    else:
        temp = temp + str(random.randrange(0,9))

print temp 
'''






import md5
h = md5.new()
h.update('admin')
print h.hexdigest()



import hashlib
hh = hashlib.md5()
hh.update('admin')
print hh.hexdigest()


