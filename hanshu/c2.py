'''
函数的定义 及 运行特点

1. 参数列表可以没有
2. 函数体里可以用 return value 返回结果  没有 则为None

定义后必须要调用  函数名()
'''


'''
1.实现两个数字的相加
2.打印输入的参数

'''
# import sys
# sys.setrecursionlimit(1000000)

def add1(x,y):
    result = x + y
    return result

def print_code(code):
    print(code)

# def print(code):
#     print(code)    
# 自己调用自己的错误
#   [Previous line repeated 995 more times]
# RecursionError: maximum recursion depth exceeded

a = add1(1,2)
# b = print_code('python')

# print(a,b)


# # 如何让函数返回多个结果

# '''

# '''

# def add1(x,y):
#     result = x + y
#     return result

# def print_code(code): 
#     print(code)
#     return   
#     #return 也能返回函数 函数内碰见 return 结束  后面的代码不会执行
#     print(code)


# a = add1(1,2)
# b = print_code('python')

# print(a,b)
