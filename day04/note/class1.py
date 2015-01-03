#!/usr/bin/evn python
#coding:utf-8
'''
#属于类的静态字段
#属于对象的动态字段
class Person:
    x = 'fly' #静态字段
    y = 'run'
#构造函数 __init__至少一个参数self
    def __init__(self,name,age,gender,se ):
        self.Name = name    #动态字段
        self.Age = age
        self.Gender = gender
        self.__secret = se         #私有字段内部调用
        self.Hand = self.__secret
    def Say(self):
        print self.__secret
        self.__Flow()
    def __Flow(self):
        #私有方法
        print 'Flow'
        
    def __del__(self):
        #析构方法
        print "qule"



tank  = Person('Tank',20,'男', 'mimimimi' )
#print tank.Age
#print Person.x
#print tank.__secret 私有字段不能直接调用，
#内部调用私有字段
#print tank.Hand

tank.Say()
'''
class Animal:
    def __init__(self):
        print 'Animal_init'
        
    def zb(self):
        print 'eatting'

class Dog(Animal):
    #Dog 是Animal 子类或者派生类
    #Animal 是Dog 父类或者基类
    def __init__(self):
        Animal.__init__(self)
        print 'Dog.__init__()'
    def Say(self):
        print '汪！！'
    
    @staticmethod #静态方法
    def  Saystatic():
        print 'luck is dog'   
dog = Dog()
print isinstance(dog, Animal)
print issubclass(Dog, Animal)
dog.zb()
#dog.Say()
Dog.Saystatic()

