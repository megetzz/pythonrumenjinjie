'''
函数参数:
    1.  必须参数
    2.  关键字参数
    3.  默认参数
    4.  
'''

'''
实际参数 
必须参数与关键字参数
必须参数  函数参数列表里面定义的参数,没有会报错
形参

'''
定义了多少形参,就要传入多少实参
最好是把参数传成对象

# 关键字参数 调用参数的时候明确指定所给的参数值给的是哪个参数
# 关键字参数 没有改变函数的行为 
#           方便提高阅读代码的理解能力  代码的可读性
#           可任意调换参数传递顺序

'''
区别 在于 函数的调用上而不在于函数的定义上 同样的定义方式 调用方式不tong

'''
def add_1(x,y):
    # 形参
    result = x + y
    return result

c  = add_1(y = 1, x = 2)

print(c)