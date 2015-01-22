#!/usr/bin/env python

import md5
from models import *

def makemd5(value):
    hash = md5.new()
    hash.update(value)
    return hash.hexdigest()

password=makemd5('123')
#arge=()
a=hosts()
b= a.GetHost(101)
print b[1]
#print a.AddHost('kali','192.168.58.128','22','mingming',password)
