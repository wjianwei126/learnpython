#!/usr/bin/env python
#coding:utf-8
import pickle
import sys
import time
#print time.strftime('%Y-%m-%d',time.localtime(time.time()))
now_day = int(time.strftime('%d',time.localtime(time.time())))
if now_day >= 10:
    lixi = (now_day -10)*0.05
else:
    lixi = (now_day + 20)*0.05

from function import login
card= raw_input('请输入信用卡帐号:')


pkl_file= open('account_info.pkl','rb')
db_dict = pickle.load(pkl_file)
pkl_file.close()

b = login(db_dict,card)
#print "当前余额 %s" % b[2]
print "取现请按1\n查询请按2\n还款请按3\n转账轻按4\n退出请按5"
c = raw_input("请输入编号：")
if int(c) == 1:
    d = int(raw_input('请输入取款金额：'))
    if d > b[2]:
        print  "超出限额请重新输入"
    else:
        #shouxu = d*0.005
        b[2] = int(b[1]) - int(d) - int(d)*0.05
        print str(b[2])
        print b
        db_dict[card] = b
        print db_dict
        b[2] = str(b[2])        
        db_dict[card]= b 
        f = file('account_info.pkl','wb')
        pickle.dump(db_dict, f)
        pkl_file.close()
        print "当前余额 %s" % b[2]
elif int(c) == 2:
    print "当前余额 %s" % b[2]
    
elif int(c) == 3:
    huankuan= raw_input('请输入还款金额：')
    b[2] =int(b[2]) + int(huankuan) - lixi
    db_dict[card] = b
    f = file('account_info.pkl','wb')
    pickle.dump(db_dict, f)
elif int(c) == 4:
    zhuanzhang = raw_input('请输入转账账户：')
    jine = raw_input('转账金额：')
    if jine > b[2]:
        print "余额不足！！"    
elif int(c) == 5:
    sys.exit()
    
else:
    print "输入错误，请重新输入"
        
