'''元字符与普通字符'''
import re


a = 'C0C++2Java4C#6Python8Javascript'

res = re.findall('\D',a)

#  '\d'数字 '\D'字母 元字符   

print(res)

