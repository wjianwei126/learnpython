#!/usr/bin/evn python
#coding:utf-8
import sys
from function import *

next = raw_input("请按'Enter'开始游戏:")+"\n"
try:
    if next== '\n':
        a = Role()
        b = Balance()
        b.first(1000)
        num = int(raw_input("请输入角色编号：").strip())
        buy = Buy()
        rolename = buy.choice(num,1000)
        c = Play(rolename)
        girlname = c.live(rolename)
        c.college(rolename, girlname)
        b.fiveyear()
        c.meet(rolename, girlname)
    else:
        print sys.exit()    
except Exception, e:
    print e
    