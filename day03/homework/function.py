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
        return a
        while i >=0 :
            password = raw_input('please input your password:')
            if passwd != password:            
                i -= 1
                print 'You have %s times ' % i
                if i == 0:
                    a[3] = '0'
                    db_dict[code]= a
                    f = file('account_info.pkl','wb')
                    pickle.dump(db_dict, f)
                    f.close()
                    sys.exit("帐号奖杯锁定")
                    break
#                   sys.exit("帐号奖杯锁定")
            else:
                print "Login success!"
                return True
                break
    else:
        print 'code is not exsit!'
        #a = db_dict[key].split(',')

def check(code):
    a=login(code)
    a[3] 

def draw(money):
    pass

    

'''
def check_passwd(code,passwd):
    passwd = login(card)
    i = 3
    
            return True

        '''