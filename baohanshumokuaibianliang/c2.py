'''
for else 循环
'''


# 主要是用来遍历/循环 序列 或者 集合 字典

a = [['apple','orange','banana','grape'],(1,2,3)]

for x in  a:
    if 'apple' in x:
        break
    for y in  x:
        if y == 'banana':
            break
        print(y)
else:
    print('EOF') #全部遍历完,会执行else


'''
a = [1,2,3]

for x in a:
    if x == 2:
        # break
        continue
    print(x)
else:
    print('EOF')
'''