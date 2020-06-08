'''类方法'''



class Student(object):
    sum = 0
    # name = ''
    # age = 12

    def __init__(self,name,age):
        self.name = name 
        self.age = age
        # 也可操作类变量
        # self.__class__.sum += 1
        # print('当前学生总数为:',str(self.__class__.sum))
        # print(self.__class__.sum += 1)


    def do_homework(self):
        # self.__class__.sum += 1
        # print('当前学生总数为:',str(self.__class__.sum))
        print('do homework')

    # self python默认传递的可以代表当前对象的参数
    def print_file(self):
        print('name'+self.name)
        print('age'+str(self.age))
    
    
    # 类方法   
    # 是否是类方法在于函数上边是否由 @classmethod 而不是看参数列表里面的名字self或cls
    # 作用:操作和类相关的变量
    # cls 代表的调用类方法的这个 类
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)
         


student1 = Student('Zz',18)
# student1.do_homework()
# 类方法调用
# Student.plus_sum() 
# 用对象调用类的方法   逻辑上说不通
student1.plus_sum()

# student2 = Student('oo',12)
# Student.plus_sum()
# # student2.do_homework()
# student3 = Student('xx',12)
# Student.plus_sum()

# student1.do_homework()
# student2.print_file()

# print(student1.name)
# print(Student.sum1)

# 类方法如何调用  类名.类方法
# Student.plus_sum()

