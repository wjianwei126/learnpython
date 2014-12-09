#!/usr/bin/env python
user = raw_input("Please input UserName:")
db = open('db.txt')
black = open('blacklist.txt', 'a')
#userlist = db.readline()
#i = 0
count = 5
for line in db:
    line = line.strip().split()
    if user in line[0]:
        passwd = raw_input("Please input password:")
        if user == line[0] and passwd == line[1]:
            print "Good Lucky"
        elif user == line[0] and passwd != line[1]:
            count -=1
            repasswd = raw_input("Please input password:")
            print "The %s'password is wrong,you can try %s times " % (user,count)
'''            while (!=line[0]):
                if count==0:
                   black.write(user)
                 if repasswd==line[1]:
                    print "Good Lucky"
                    break
'''
#else:
#    print "The username not exit,Please check again."
