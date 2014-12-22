#!/usr/bin/env python
#_*_coding:utf8_*_
import sys
#import fun
#from fun import add_user, del_user, update_info, search_info

f = file('stu_list.txt')
stu_dic={}

for id,line in enumerate(f):		#枚举行号
    stu_dic[id] = line.strip()		 #把行号主键存入字典
f.close()

f2 = file('stu_list.txt')			#第二次打开文件
user_dic = {}						#定义空字典
for line in f2.readlines():			#循环取每行的值	
    username = line.strip()			#定义列表
    user = username.split(' ')		#按空格切割保存到列表
    user_dic[user[0]] = user[1]+' '+user[2]+' '+user[3]   #用户名作为主键存入字典
f2.close()

do = raw_input("Please input ADD , DEL ,UPDATE OR SEARCH:")   #用户输入选择

if do == 'ADD':    #如果添加用户
    user_input = raw_input("Please input username:")  #请输入要插入的用户名
    if len(user_input) < 3:
        sys.exit("The username too short!")
    f3 = file('stu_list.txt', 'a' )				#第三次打开文件 追加
    if user_dic.has_key(user_input):			#判断输入用户是否在字典中
        print "user exsit!"						#如果在输入已存在	
    else:										#输入不存在继续
        age = int(raw_input('User age:'))			#输入年龄
        if len(str(age)) < 1:
            sys.exit("please input age number:")
        tel = int(raw_input('Tel Phone:'))			#电话
        if len(str(tel)) < 10:
            sys.exit("phone number is wrong.")
        corporation = raw_input('Corporation:')			#公司名称
        if len(corporation) < 3:
            sys.exit("please replace input:")
        email = raw_input('email:')						#邮箱地址
        f3.write("%s %s %s %s %s\n" %(user_input,age,tel,corporation,email))	#按行写入文件
        #user_dic[user_input] = age+' '+tel+' '+corporation+' '+email
        f3.close()							#关闭文件
elif do == 'DEL':		#如果正确执行删除
    user_input = raw_input("Please input the username you want delete:")		#要删除的用户名
    f4 = file('stu_list.txt','w')		#第四次写模式打开
    if user_dic.has_key(user_input):		#如果存在字典中
        del user_dic[user_input]			#删除key
        for key in user_dic:				#循环字典中的key
            #print key		
            f4.write(key+' '+user_dic[key]+'\n')		#key，value写入到数据文件
        f4.close()			#关闭文件
    else:			#如果不存在
        print "Username is not exist!!"				#提示不存在
elif do == 'UPDATE':				#如果Update
    user_input = raw_input("Please input the username you want update:")	 #输入用户
    f5 = file('stu_list.txt','w')		#第五次打开
    if user_dic.has_key(user_input):	#判断在字典中
        age = int(raw_input('User age:'))		#输入年龄
        if len(str(age)) < 1:
            sys.exit("please input age number:")
        tel = int(raw_input('Tel Phone:'))			#电话
        if len(str(tel)) < 10:
            sys.exit("phone number is wrong.")
        corporation = raw_input('Corporation:')		#公司名称
        if len(corporation) < 3:
            sys.exit("please replace input:")
        email = raw_input('email:')				#邮箱地址
        user_dic[user_input] = str(age)+' '+str(tel)+' '+corporation+' '+email	#存入字典
        for key in user_dic:					#循环字典
            f5.write(key+' '+user_dic[key]+'\n')		#写入数据文件
        f5.close()				#关闭文件
    else:						#如果不存在
        print "Username is not exist!!"		#提示不存在
else:			#其他情况
    while True:		#开始模糊查询
        mathc_list = {}		#定义空字典
        choice = raw_input('Search info:')  	#输入查询信息
        if choice == 'exit':break		#exit
        if stu_dic.has_key(choice):			#存在
            mathc_list[choice] = stu_dic.get(choice)   #写入到mathc_list
            #print mathc_list
        choice = str(choice)			#输入转换成字符串

        if len(choice) >= 3:			#字符串大于等于3
            for id,val in stu_dic.items():		#在列表中循环key ，value
                if str(choice) in val:			#判断字符串在Value中存在
                    mathc_list[id] =val			#赋值到mathc_list字典
        for k,v in mathc_list.items():			#在字典中循环关键字
            print k,v							#输出关键字
