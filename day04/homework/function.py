#!/usr/bin/env python
#coding:utf-8
import time
import sys
class Balance:
    def __init__(self):
        pass
    def first(self,wealth):
        self.Wealth =  wealth
        print "当前游戏币余额 %s" % wealth
        return wealth
        
    def fiveyear(self,wealth=20000000):
        print '经过多年的奋斗你身价已经达到%s' % wealth
        

class Role(Balance):
    
    def __init__(self):
        print "欢迎开始游戏，角色介绍："
        print "1 Jhon男性，坚强能干，会有勤劳加成。$800"
        print "2 Liza女性，初级阶段收到众多男士爱慕，美丽加成$1100"
        print "3 Peter继承原始资产，升级快速$5000"
        print "更多新角色即将上线敬请期待……"
'''
    def RoleNum(self,number):
        self.RoleNum=number
        if number == 1:
            print "恭喜你成功购买了'Jhon'"
        elif number ==2:
            print "恭喜你成功购买了Liza"
        elif number == 3:
            print "Perter"
        else:
            print "更多角色请期待"
    '''    
class Buy(Balance):
    def balance_money(self,balance_money,choice_role):

        if balance_money >= 0:
            print "恭喜你成功购买了 %s" % choice_role
            print "当前余额%s" % balance_money
        else:
            print "余额不足，请前往充值"
            enter = raw_input()+'\n'
            sys.exit('充值系统正在维护，请稍候')
                
    def choice(self,number,wealth):
        a =Buy()
        if number ==1:
            balance_money = wealth -800
            choice_role = 'Jhone'
            a.balance_money(balance_money, choice_role)
            return choice_role
        elif number ==2:
            choice_role = 'Liza'
            balance_money = wealth - 1200
            a.balance_money(balance_money, choice_role)
            return choice_role
        elif number ==3:
            balance_money = wealth - 1600
            a.balance_money(balance_money, choice_role)
            return choice_role 
        else:
            sys.exit("更多角色敬请期待")


class Play():
    
    def __init__(self,rolename):
        print "欢迎开始你的人生%s,请选择任务\n1 去上学\n2 去打工 " % rolename
        choice_next = int(raw_input("请输入任务编号："))
        if choice_next ==1:
            print '欢迎来到学校开始新的人生……'
        else:
            sys.exit("更多任务开发中")
            
            
    def live(self,you):
        enter = raw_input()+'\n'
        agirl = raw_input("有一天你遇到了一个女孩，她的名字叫：").strip()
        while len(agirl) <3:
            agirl = raw_input("请重新输入，她的名字叫：").strip()
            continue
        else:
            pass
        print '通过重重障考验，%s战胜了所有情敌，把%s追到手,幸福的在一起你们相约一起考上北大' % (you,agirl)
        enter = raw_input()+'\n'
        print '但是……'
        print '%s发挥失常没有考上北大' % you
        return agirl
    def college(self,you,agirl):
        print '%s来到%s的城市，通过打工赚金币，供给%s学费,一直到毕业' % (you,agirl,agirl)
        enter = raw_input()+'\n'
        print "%s找到了一份新的工作，她的薪水比你的多，直到有一天，他的老板Peter开始追求她" % agirl
        enter = raw_input()+'\n'
        print "她最终选择离你而去...,和Peter苟且在一起"
    
        print '%s清楚Peter从他父亲继承金币远多余你现有的，你离开了这里，换了电话号码，开始学习，努力工作，赚更多的金币' % you
        enter = raw_input()+'\n'
    def meet(self,you,agirl):
        print '五年后的一天'
        enter = raw_input()+'\n'
        print '一个偶然的机会在马航的飞机上，你再次见到了%s' % agirl
        enter = raw_input()+'\n'
        print '未完待续…………'
        
 


     

