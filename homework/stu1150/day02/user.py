#!/usr/bin/env python
#_*_coding:utf8_*_
import fun
from fun import add_user, del_user, update_info, search_info
print "Please input add, del, update,check as next."

input = raw_input("what's do you want?")
if input == 'add':
    add_user()
