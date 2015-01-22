#!/usr/bin/evn python
#coding:utf-8


import  json

a = {'k1':'v1','k2':'v2'}

a_json = json.dumps(a)
print a_json
print type(a_json)

a_new = json.loads(a_json)
print a_new
print type(a_new)