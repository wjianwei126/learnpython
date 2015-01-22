dict = {}
f = file('stu_list.txt')
for line in f.readlines():
    username = line.strip()
    user = username.split(' ')
    dict[user[0]]= user[1]+' '+user[2]+' '+user[3]
a = raw_input("username please:")
if dict.has_key(a):
    print "exist"
