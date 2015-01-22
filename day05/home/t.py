#!/usr/bin/evn python
#coding:utf-8

import md5


def makemd5(value):
    hash = md5.new()
    hash.update(value)
    return hash.hexdigest()


print makemd5('data')