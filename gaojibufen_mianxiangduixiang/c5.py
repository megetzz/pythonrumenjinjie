'''
# __dict__ 保存当前对象的所有相关变量
类与对象的变量查找顺序

'''

class Student(object): #类是抽象的 实例是具体的
# 类变量  和 实例变量不同   某个类的属性
    name = 'pp'   
    age = 0

# 79406503

    def __init__(self,name,age):   #最常见的是初始化类的特征值
        # 构造函数
        # 初始化对象的属性  
        # 构造函数的赋值没有改变 变量的取值
        # 实例变量用self获取
        self.name = name
        self.age = age

    def do_homework(self):
        print('homework')


    def print_file(self):
        print('name:' + self.name)
        print('age:' + str(self.age))

student1 = Student('Zz',18)
student2 = Student('oo',12)

# python 寻找相关变量的机制
#  如果尝试寻找某个相关变量 
# python 首先会在对象的实例变量的列表里面 查找这个变量
# 如果没有 到类变量的列表里寻找
# 如果在类里边也没找到  会到父类里边寻找  （继承）

print(student1.name)

# print(student2.name)
# print(student2.age)
print(Student.name)

# __dict__ 保存当前对象的所有相关变量
print(student1.__dict__)
# Student 类
print(Student.__dict__)


'''
# 类由自己的规则和特性

# '类变量'
# 和类相关的变量

# '实例变量'
# 实例变量和对象相关联在一起
# 对象是由类模板创建出来的
# 实例变量用 self 变量 构成
'''