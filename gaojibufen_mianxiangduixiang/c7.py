'''在实例方法中访问实例变量和类变量'''


class Student(object): #类是抽象的 实例是具体的
# 类变量  和 实例变量不同   某个类的属性
    name = 'pp'   
    age = 0
    sum1 = 0

# 79406503

#  定义要self 默认传入 和调用不同
    def __init__(self,name1,age):   #最常见的是初始化类的特征值
# 构造函数可以看作特殊的实例方法
# 和实例方法的区别在于调用的方式是不样的

# 意义： 初始化类的各种特征
        self.name = name1
        self.age = age
        # 实例方法里正确访问类变量e的方式:
        print(Student.sum1)
        # 第二种 self内置的__class__代表的类
        print(self.__class__.sum1)

        # print(self.name)
        # print(self.__dict__) 
        #python 
        # 查找机制仅在类对象外部调用的时候生效
        # 访问实例变量的时候加self

        # print(self.age)
        # print(name)  #读取的是形参name
        
# 实例方法  描述类的行为
    def do_homework(self):
        print('homework')


    def print_file(self):
        print('name:' + self.name)
        print('age:' + str(self.age))


# 实例方法里面访问类变量
student1 = Student('Zz',18)
# student2 = Student('oo',12)
# student1.do_homework()

# student2.print_file()

print(student1.name)


print(Student.sum1)


# print(student1.__dict__)
# Student 类
# print(Student.__dict__)
