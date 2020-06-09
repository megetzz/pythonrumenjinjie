'''字符集'''
import re

s = 'abc, acc, adc, aec, afc, ahc'

#找出中间字母是c或f的
res = re.findall('a[c-f]c',s)
print(res)

'''字符集的特性 出现在[]里的字符之间的关系是或'''
'''  加 ^ 取反'''
# 如果太多的话可以用字符顺序省略之间的字符