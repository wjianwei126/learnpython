#!/usr/bin/env python
#coding:utf-8
import pickle
import sys
'''
db_dict = { '800':'pass,15000,15000,0',
            '900':'passwd,15000,15000,1',
            '700':'password,15000,15000,1',
            '400':'paass,15000,15000,1',}

f = file('account_info.pkl','wb')
pickle.dump(db_dict, f)
f.close()
'''
pkl_file= open('account_info.pkl','rb')
db_dict = pickle.load(pkl_file)
pkl_file.close()
print db_dict
print '----------------------'

def login(code):    
    if db_dict.has_key(code):
        a = db_dict[code].split(',')
        if int(a[3])== 0:
            sys.exit("Your account was clocked,please send email to administrator.")
        passwd = a[0]
        i = 3
        while i >=0 :
            password = raw_input('please input your password:')
            if passwd != password:            
                i -= 1
                print 'You have %s times ' % i
                if i == 0:
                    a[3] = '0'
                    db_dict[code]= a[0]+','+a[1]+','+a[2]+','+a[3]
                    f = file('account_info.pkl','wb')
                    pickle.dump(db_dict, f)
                    f.close()
                    sys.exit("帐号奖杯锁定")
                    break
 #                   sys.exit("帐号奖杯锁定")
            else:
                print "Login success!"
                return a
                break
    
    else:
        print 'code is not exsit!'
        #a = db_dict[key].split(',')


def draw(code):
    b = login(code)
    print b 
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
            db_dict[code] = str(b[0])+','+str(b[1])+','+str(b[2])+','+str(b[3])
            print db_dict
            #b[2] = str(b[2])        
            #db_dict[code]= b 
            #f = file('account_info.pkl','wb')
            #pickle.dump(db_dict, f)
            print "当前余额 %s" % b[2]
    elif int(c) == 2:
        print "当前余额 %s" % b[2]
    
    elif int(c) == 3:
        huankuan= raw_input('请输入还款金额：')
        b[2] =int(b[2]) + int(huankuan)
        print "当前可用余额%s" % b[2]
    elif int(c) == 4:
        zhuanzhang = raw_input('请输入转账账户：')
        jine = raw_input('转账金额：')
        if jine > b[2]:
            print "余额不足！！"    
    elif int(c) == 5:
        sys.exit()
    
    else:
        print "输入错误，请重新输入"

#login('700')

    

'''
def check_passwd(code,passwd):
    passwd = login(card)
    i = 3
    
            return True

        '''