#!/usr/bin/env python
#_*_coding:utf8_*_



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
    user_dic[user[0]]= user[1]+' '+user[2]+' '+user[3]

user_input = raw_input("Please input username:")
if user_dic.has_key(user_input):
    print "user exsit!"
else:
    print "add user"

def search_info():
    choice = raw_input('Search info:')
    mathc_list = {}
    #if choice == 'exit':
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
    pass

