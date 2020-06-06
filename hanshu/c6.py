'''
默认参数
定义的时候 
    如果使某个值有默认值,只需在形参后面加'='并赋值

调用的时候 
    如果没有给某个形参设置默认值,必须在函数调用的时候传
如果改变其中某个形参的默认值,就正常传参
'''

''' 必须传的参数 和 可选的默认参数
不能把非默认参数放到默认参数之后,
也就是所有的必须传的参数放到最前边
后面的参数必须是默认参数
不能出现混杂的参数,否则会报错

'''




# 设置默认值 在形参后面田默认的值
# 有固定值的时候 使用默认参数 简化函数的调用
def print_student_files(name,gender='男',age='18',
college='家里'):
    print('我叫'+name)
    print('今年'+str(age)+'岁')
    print('我是'+gender+'生')
    print('我在'+college+'上班')

print_student_files('李四','男','18','家里')
print('*'*20)
print_student_files('张三')
print('*'*20)
print_student_files('王五','女',16)
print('*'*20)
# 按形参列表的顺序放进实参列表里 
# 解决方法  标识具体的参数  可以不遵守顺序 
print_student_files('大力',age=17,college='滨河路',gender='女')
print('*'*20)
# 按默认参数列表传参 不能把默认值参数和必须参数混杂调用
print_student_files('大力',gender='女',18,college='天上')