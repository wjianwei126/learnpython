#!/usr/bin/env python
#_*_coding:utf8_*_

f = file('stu_list.txt')
stu_dic={}

#serch = raw_input('Input Serch info:')

for id,line in enumerate(f):
    stu_dic[id] = line.strip()
#    print stu_dic

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
    #        print id,val
            if str(choice) in val:
                mathc_list[id] =val
#    print mathc_list
    for k,v in mathc_list.items():
#        print k,v.replace(choice,'\033[32;1m%s\033\EM]') %  choice
        print k,v

