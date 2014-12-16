#!/usr/bin/env python

import sys
user = raw_input("Please input UserName:")
add_black = open('blacklist.txt', 'a')
check_black = open('blacklist.txt')
count = 5
db = { 'mingming':'123456','aaa':'aaa','bbb':'bbb' }
#if line in f:
for line in check_black:
    if user in line:
        check_black.close()
        sys.exit( "Sorry your account was clocked!!Go away!!")
    else:
        pass

if user in db:
        while True: 
            passwd = raw_input("Please input password:")
            if passwd== db[user]:
                print "Welcom to Home %s !!!" % user
                break
            else:
                count -=1
                print "%s'password is wrong,you can try %s times " % (user,count)
                if count == 0:
                    print "Warming Username will clocked."
                    add_black.write(user+'\n')
                    add_black.close() 
                    break
                elif count < 1:
                    sys.exit()
                else:
                    continue
else:
    sys.exit("The username not exist,Please check again.")
