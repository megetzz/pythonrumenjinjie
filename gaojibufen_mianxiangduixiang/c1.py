'''
面向对象

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
# 类定义

class Student(object):
    name = ''   
    age = 0
    
    # 类下面的函数叫方法 
    def print_file(self):
        print('name:' + self.name)
        print('age:' + str(self.age))

# class StudentHomework():
#     homework_name = ''


    
# 调用   
# 实例化   类名+括号
student = Student()
# 如何调用类下面的方法?
student.print_file()