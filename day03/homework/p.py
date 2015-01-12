#!/usr/bin/env python
import pickle
'''
account_info = { '0101' :'aaaa',
                '0102':'bbbb'}

f = file('acout.pkl','wb')
pickle.dump(account_info,f)
f.close()



pkl_file= open('acout.pkl','rb')

account_list = pickle.load(pkl_file)
pkl_file.close()
print account_list

'''

db_dict = { '1':'800,pass,15000,15000',
            '2':'900,passwd,15000,15000',
            '3':'700,password,15000,15000',
            '4':'400,paass,15000,15000'}

f = file('account_info.pkl','wb')
pickle.dump(db_dict, f)
f.close()
           
#a = db_dict[1].split(',')
#print a[0]