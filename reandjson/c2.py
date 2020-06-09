import re

a = 'C|C++|Java|C#|Python|Javascript'

# re.findall('正则表达式'，字符串)


r = re.findall('Python',a)
# re 的精髓 在于规则
print(r)
if len(r) > 0:
    print('字符串中包含Python')
else:
    print('No')


# print(a.index('Python')>-1)

# print('Python' in a)