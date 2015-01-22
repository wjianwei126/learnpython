#!/usr/bin/env python 
#_coding_:utf-8_*_

'''
li = []
help(li)

import a
reload(module)


print dir()
print vars()


print abs(-5)

print cmp(2,2)

print divmod(59,9)


print pow( 2,11)

s = 'test {0}'

print s.format('nimei')


li = [1,2,3]
def Func(arg):
    return arg + 10

li_new=map(Func, li)
print li_new


li = [1,2,3,4,5,6,7,8]
def Func(arg):
    if arg > 5:
        return True
    else:
        return False

li_new=filter(Func, li)
print li_new
'''

def Function(arg):
    if arg >2:
        return True
    else:
        return False


def Myfilter(func,arg):
    var_li = []
    if func ==None:
        return arg
    else:
        for item in arg:
            re = func(item)
            if re == True:
                var_li.append(item)
                
        return var_li

li = [1,2,3,4,5]
print Myfilter(Function, li)














