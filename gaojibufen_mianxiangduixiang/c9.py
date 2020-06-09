'''静态方法'''


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
student1.__score = 59  #如果赋值 建议通过方法

# r = student1.score
# print(r)

# 不要直接在对象外部对成员变量进行赋值,如果要赋值,建议通过方法,
# 原因在于可以在方法里面对对象已输入的参数进行判读,
# 如果不符合它的数据状态的要求,超出了范围.可以保护数据

# 如果一个类下面有好多个变量

# 有没有方法可以阻止在外部对变量进行赋值或读取操作?
# 成员可见性问题 
# 公开的 public   赋值  读取
# 私有的 private  在外部无法直接读取或赋值设置
# 为什么此demo所有变量方法都是公开的?  其他语言的前缀加上public 代表公开的 加上private 是私有的 不能从外部直接访问
# python 没有 public private 没有这两个关键字代表公开私有 
# python 用 双下划线 __xxx 来标识方法或变量是私有 没有__是公开的

# 为什么构造函数前面有双下划线 能从外部访问?
# python特有的函数或变量, 允许从外部进行访问 前后都是双下划线
# 内置的命名风格  个人应极力避免

