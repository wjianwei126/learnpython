#!/usr/bin/evn python
#coding:utf-8
#������ʽ
'''
re.complile()
re.match()
re.search()
re.finedall()

group()
groups()

re.split()
re.sub()
'''
import re

nret1 = re.match('hi','hihihisssssssssssssssssfaf')
print nret1.group()

cmp = re.compile('hi')
mat = cmp.match('hihihihihiasdfa')
print mat.group()


nret2 = re.search('hi', 'aaahaihihiahihih')
print nret2.group()

nret3 = re.findall('hi', 'asfddhihihi')
print nret3


print re.split('\d+', 'asfdasf1231241m1241243123_123')
s = 'a11b22c33'
print s.split('22')


print re.sub('\d+', '_','a11b22c33d' )
s = 'a11b22c33'
print s.replace('33', 'xx')
