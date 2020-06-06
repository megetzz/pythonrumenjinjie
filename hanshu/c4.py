'''序列解包 与 链式赋值
'''

# a = 1
# b = 2
# c = 3

a,b,c = 1,2,3

d = 1,2,3
print(type(d)) 

a,b,c = d
print(d)

a = b = c = 1
print(a,b,c)