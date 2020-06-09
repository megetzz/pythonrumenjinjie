'''
继承
面向对象重要的特征之一 继承
作用:    1.避免定义重复的方法和重复的变量(面向对象的语法层面 )
    类由两大块组成   类的特征(实例变量 类变量)
                行为(各种方法)
        2.事物之间的关系(现实)

有意义的继承 ?

python 可以多继承 一个子类继承多个父类



子类调用父类方法 super()


'''
# 一个文件定义一个类  
from c12 import Human  

class Studnet(Human):  #括号()里的类是当前的父类  外边的是里边的子类
# 通常来说 子类有自己的变量

    # sum = 0
    
    def __init__(self,school,name,age):   
        self.school = school
        #子类的name age 传给父类 在 子类的构造函数里边
        # 非常奇怪的调用 类调用实例方法  python内部的实例化机制自动调用的 不正确 面向对象上 
        # Human.__init__(self,name,age) #普通方法的调用 #调用父类的实例方法加上 self， 

# super 关键字  super(当前类 ，self).构造函数/实例方法（）
        super(Studnet,self).__init__(name,age)


        # self.__score = 0
        # self.__class__.sum += 1



    def do_homework(self):
        
        print('do english homework')
        super(Studnet,self).do_homework()

studnet1 = Studnet('家里蹲大学','pP',12)
# Studnet.do_homework(studnet1)#  ????????
studnet1.do_homework()

# 不论哪种调用方式,子类都继承了父类
# print(studnet1.sum)    
# print(Studnet.sum)    
# print(studnet1.name)    
# print(studnet1.age)    

# studnet1.get_name() 