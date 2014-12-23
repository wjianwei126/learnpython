#!/usr/bin/env python
#coding:utf-8

from function import login
card= raw_input('Please input yout cardcode:')

if login(card):
    
        
    


    
'''
def login(code):
    f = file('code.txt')
    dict = {}
    i = 3
    for line in f.readlines():
        a = line.strip().split('\t')
        dict[a[0]] = a[1]
    #if  dict.has_key(code):
        return dict
    else:
        return False

        password =raw_input('please input your pass:')
        while i > 0:
            if dict[code] == password:
                print 'password is right!'
            else:
                i -=1
                break
            print "you have %s times input" % i

             
            
        #if dict[code] == password:
        #    return True
        #else:      

        
'''