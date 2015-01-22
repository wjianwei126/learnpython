#!/usr/bin/evn python
#coding:utf-8

import json
import pickle

def sarilize(arg,obj):
    #以字符串模式导入模块
    '''module = __import__(arg)
    return module.dumps(obj)
    '''
    #以字符串方式执行函数
    module = __import__(arg)
    func = getattr(module, 'dumps')
    return func(obj)
    '''
    if arg == 'json':
        str_j = json.dumps(obj)
        return str_j
    else:
        str_p = pickle.dumps(obj)
        return str_p
    '''
obj = [1,2,3,4,]
print sarilize('pickle', obj)
#load 反射实现