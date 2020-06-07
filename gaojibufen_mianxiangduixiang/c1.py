'''
面向对象
类  对象
实例化
封装

类和对象 是什么 之间的关系 理解 
关注的是实例化的那部分
类和对象的关系通过实例化联系在一起

# 有意义的面向对象的代码

核心?  
类 = 面向对象
理解面向对象最基础的核心 
什么是类 什么是对象  两者关系
封装一系列的变量 一系列的函数
最基本作用:
    封装 

类 只负责定义或刻画一些东西
'''

'''
python 使用 关键字 class 定义一个类 
class 类名
命名规则和变量命名规则有所不同 
第一个字母 大写
变量使用下划线连接
类用大驼峰命名法
'''
# 不要在一个模块里 即定义类 又实例化和调用
'''
方法 函数 的区别
没有绝对的区别  很多时候是模糊这两个
C C++   习惯于称作 函数 
Java C# 习惯于称作 方法

方法是设计层面上的一个称呼 更多是面向对象的一个概念 面向对象更加关注设计,设计代码结构,设计代码封装.
函数: 更多是面向过程的一个概念.程序运行 过程式的一种称谓
'''
# 类定义
'''
什么是类 
类是现实世界或思维世界中的实体 在计算机中的反映
它将数据以及这些数据上的操作封装在一起


'''
'''
类里面定义的函数应该称作方法 面向对象的最基本的概念,更加关注设计层面
把函数定义在模块里,不要称作方法 还是称作函数

'''

'''
类下面定义的变量  
py 更多时候称为 数据成员
在于体现类的封装
每个变量都被视作类的数据,这个数据用来描述类的特征
'''

'''
类就像模板,通过各种各样的具体值 类可以产生很多对象 
'''

# 类 一类事物的总称 并不是一个具体  当类实例化后 就变成具体的对象
# 学生类
class Student(object):
    # 类下面定义的变量在模块里面 可以称谓 变量 or 数据成员
    # 特征 属性

    name = ''   
    age = 0

# 构造函数的调用是自动进行的  当实例化的时候 python自动调用 __init__ 构早函数'''
# 构造函数的作用 让模板生成不同的对象
    def __init__(self,name,age):   #最常见的是初始化类的特征值
        # 初始化对象的属性  
        # 构造函数的赋值没有改变 变量的取值
        name = name
        age = age
        # print('student',name,age)

# 实例化以及实例化的意义

    
    # 行为  def 方法
    def do_homework(self):
        print('homework')
    
    #  行为  能做什么事情
    # 行为与特征  设计类 

    # 类下面的函数叫方法 
    
    def print_file(self):
        print('name:' + self.name)
        print('age:' + str(self.age))

# class StudentHomework():
#     homework_name = ''


    
# 调用   
# 实例化   类名+括号
# student = Student()
# 如何调用类下面的方法?
# student.print_file()


# 把握行为的主体是什么???

'''# 打印类'''
# class Printer():

#     def print_file(self):
#         print('name:' + self.name)
#         print('age:' + str(self.age))



# 内存地址不同
student1 = Student('Zz',18)
print(student1.name)
# a =  student1.__init__()
# print(a)
# print(type(a))
# student2 = Student()
# student3 = Student()

# student1.print_file()
# print(id(student1))
# print(id(student2))
# print(id(student3))