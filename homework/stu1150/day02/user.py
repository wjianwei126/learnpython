#!/usr/bin/env python
'##_*_coding:utf8_*_'
import sys
#import fun
#from fun import add_user, del_user, update_info, search_info

f = file('stu_list.txt')
stu_dic={}

for id,line in enumerate(f):
    stu_dic[id] = line.strip()
f.close()

f2 = file('stu_list.txt')
user_dic = {}
for line in f2.readlines():
    username = line.strip()
    user = username.split(' ')
    user_dic[user[0]] = user[1]+' '+user[2]+' '+user[3]
f2.close()

do = raw_input("Please input ADD , DEL ,UPDATE OR SEARCH:")

if do == 'ADD':
    user_input = raw_input("Please input username:")
    f3 = file('stu_list.txt', 'a' )
    if user_dic.has_key(user_input):
        print "user exsit!"
    else:
        age = raw_input('User age:')
        tel = raw_input('Tel Phone:')
        corporation = raw_input('Corporation:')
        email = raw_input('email:')
        f3.write("%s %s %s %s %s\n" %(user_input,age,tel,corporation,email))
        #user_dic[user_input] = age+' '+tel+' '+corporation+' '+email
        f3.close()
elif do == 'DEL':
    user_input = raw_input("Please input the username you want delete:")
    f4 = file('stu_list.txt','w')
    if user_dic.has_key(user_input):
        del user_dic[user_input]
        for key in user_dic:
            print key
            f4.write(key+' '+user_dic[key]+'\n')
        f4.close()
    else:
        print "Username is not exist!!"
elif do == 'UPDATE':
    user_input = raw_input("Please input the username you want update:")
    f5 = file('stu_list.txt','w')
    if user_dic.has_key(user_input):
        age = raw_input('User age:')
        tel = raw_input('Tel Phone:')
        corporation = raw_input('Corporation:')
        email = raw_input('email:')
        user_dic[user_input] = age+' '+tel+' '+corporation+' '+email
        for key in user_dic:
            f5.write(key+' '+user_dic[key]+'\n')
        f5.close()
    else:
        print "Username is not exist!!"
else:
    while True:
        mathc_list = {}
        choice = raw_input('Search info:')
        if choice == 'exit':break
        if stu_dic.has_key(choice):
            mathc_list[choice] = stu_dic.get(choice)
            print mathc_list
        choice = str(choice)

        if len(choice) >= 3:
            for id,val in stu_dic.items():
                if str(choice) in val:
                    mathc_list[id] =val
        for k,v in mathc_list.items():
            print k,v
