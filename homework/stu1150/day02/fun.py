#!/usr/bin/env python
#_*_coding:utf8_*_

def user_dic():
    f2 = file('stu_list.txt')
    user_dic = {}
    for line in f2.readlines():
        username = line.strip()
        user = username.split(' ')
        user_dic[user[0]]= user[1]+' '+user[2]+' '+user[3]
    f2.close()


def add_user():
    user_dic()
    user_input = raw_input("Please input username:")
    f3 = file('stu_list.txt', 'a' )
    if user_dic.has_key(user_input):
        print "user exsit!"
    else:
        age = raw_input('User age:')
        tel = raw_input('Tel Phone:')
        compate = raw_input('Compane:')
        email = raw_input('email:')
        f3.write("%s %s %s %s %s\n" %(user_input,age,tel,compate,email))
        #user_dic[user_input] = age+' '+tel+' '+compate+' '+email
        f3.close()
    
def del_user():
    user = raw_input("Please input the user:")

def update_info():
    print "change"

def check_user():
    f2 = file('stu_list.txt')
    user_dic = {}
    for line in f2.readlines():
        username = line.strip()
        user = username.split(' ')
        user_dic[user[0]]= user[1]+' '+user[2]+' '+user[3]
    return user_dic

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
