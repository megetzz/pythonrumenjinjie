'''
self 与 实例方法

实例方法定义的时候self必须出现
调用实例方法的时候不需要self传参
python 必须强制指定self 也可以改成自己的 例如this self是python建议的  python 之禅的 显胜于隐

self是什么 
self是当前调用某一方法的对象
谁调用的这个方法，self就指代的谁 self代表的是实例而不是类
self必须要写

实例方法
实例变量和对象（类生成的实例）相关联
实例方法和对象和实例相关联
实例可以调用的方法叫实例方法
最大的特点是第一个参数传入一个self




'''


class Student(object): #类是抽象的 实例是具体的
# 类变量  和 实例变量不同   某个类的属性
    sum = 0
    name = 'pp'   
    age = 0

# 79406503

#  定义要self 默认传入 和调用不同
    def __init__(self,name,age):   #最常见的是初始化类的特征值
        # 构造函数
        # 初始化对象的属性  
        # 构造函数的赋值没有改变 变量的取值
        # 实例变量用self获取
        self.name = name
        self.age = age
        print(name)
        print(age)
# 实例方法 
    def do_homework(self):
        print('homework')


    def print_file(self):
        print('name:' + self.name)
        print('age:' + str(self.age))

student1 = Student('Zz',18)
student2 = Student('oo',12)
student1.do_homework()
student2.print_file()
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