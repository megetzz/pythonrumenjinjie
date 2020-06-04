# 判断某个字符在字串里
def exsit(a,b):
    # a 输入的字符 b 查询的字符 
    a = set(a)
    return b in a
a = 'abc'
b = 's'
print(exsit(a,b))