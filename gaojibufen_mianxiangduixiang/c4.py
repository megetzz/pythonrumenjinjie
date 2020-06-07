'''

区别模块变量与类中的变量


# 模块
# python中的局部变量不会覆盖全局变量
# 局部变量的作用域在 函数内部
# 全局变量的值不会因为局部变量而更改


# 类中的不一样

'''


class Student(object): #类是抽象的 实例是具体的
# 类变量  和 实例变量不同   某个类的属性

    name = ''   
    age = 0

    # sum 所有学生的总数
    sum = 0

# 类由自己的规则和特性

# '类变量'
# 和类相关的变量

# '实例变量'
# 实例变量和对象相关联在一起
# 对象是由类模板创建出来的
# 实例变量用 self 变量 构成

# 79406503

    def __init__(self,name,age):   #最常见的是初始化类的特征值
        # 构造函数
        # 初始化对象的属性  
        # 构造函数的赋值没有改变 变量的取值
        self.name = name
        self.age = age
        
        print(name)
        print(age)
        # 在方法里能不能访问类的变量

    def do_homework(self):
        print('homework')


    def print_file(self):
        print('name:' + self.name)
        print('age:' + str(self.age))

student1 = Student('Zz',18)
student2 = Student('oo',12)
print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
# print(Student.name)