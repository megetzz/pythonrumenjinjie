'''
没有什么是不能访问的
私有变量强行从外部赋值不会报错?


严格意义上 python没有私有变量 
通过魔术方法读取被更换的私有变量  
没有任何记住读取私有变量
不应该强制读取
'''

class Student(object):
    sum = 0
    name = ''
    age = 12

    def __init__(self,name,age):
        self.name = name 
        self.age = age
        self.__score = 0
        # 也可操作类变量
        self.__class__.sum += 1
        # print('当前学生总数为:',str(self.__class__.sum))
        # print(self.__class__.sum += 1)

      

    def marking(self,score):
        if score < 0:
            score = 0 
            # print('成绩不能为负数')
            return '输入错误,不能打负分'
        self.__score = score
        print(self.name + '本次成绩为:'+str(self.__score)+'分')



# 内部调用: 在类的内部 一个函数可以调用另外的函数
# 外部调用: 在外部 实例化后的
    def do_homework(self):
        # self.__class__.sum += 1
        # print('当前学生总数为:',str(self.__class__.sum))
        self.do_english_homework()
        print('do homework')
         

    def do_english_homework(self):
        print('do english homework')

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
        # print(name)

    # 静态方法 装饰器@staticmethod
    # 静态方法没有强制默认传入指定的名字例如self cls
    @staticmethod
    def add(x,y):
        # 静态方法内部访问类变量
        print(Student.sum)
        # print('this is a static method静态方法')
        # print( name)
 

student1 = Student('Zz',18)
student2 = Student('Xx',18)

# 外部访问

student1.do_homework()
# 类方法调用
# Student.plus_sum() 
# 用对象调用类的方法   逻辑上说不通
# student1.plus_sum()

# 类和对象都可以调用静态方法
student1.add(1,2)
Student.add(1,2)
student1.plus_sum()  #对象访问类方法

result = student1.marking(59)
print(result)
#如果赋值 建议通过方法
student1.__score = -1  
#### python动态语言的特性 ,给student1对象新添加了一个新属性__score,不是设置的实例变量__score
# 不可以动态添加私有属性 

print(student1.__score)
print(student1.__dict__)   #python 存储私有变量做的更改 (类名+__xx )'_Student__score': 59,
# {'name': 'Zz', 'age': 18, '_Student__score': 59, '__score': -1}
# print('-'*20)
# print(student2.__score)  # 报错 
print(student2.__dict__)
print(student2._Student__score)