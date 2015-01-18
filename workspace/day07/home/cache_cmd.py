#/usr/bin/env python
#coding:utf-8

import os
import re
import os.path

file_list= os.listdir('./scripts/redmine/')

for i in file_list:
    #print i
    #print os.path.basename('./scripts/redmine/%s' % i)    
    filename ='./scripts/redmine/'+i
    f = file(filename)
    f.readline()
