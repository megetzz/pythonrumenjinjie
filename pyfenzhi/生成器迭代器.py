'''可迭代对象  -> 迭代器
所有的容器都是可迭代的(iterable)
迭代器(iterator) 提供了一个 next 方法 //或者得到下一个元素,或者StopIteration的错误

通过iter() 方法 把可迭代对象 变成 迭代器
通过next()  方法 得到
导包 from collections import Iterable  
通过 isinstance(object,iter) 方法 
'''

from collections.abc import Iterable
from collections.abc import Iterator

print(isinstance([1,2,3],Iterable))
print(isinstance([1,2,3],Iterator))

'''
生成器是懒人版本的迭代器 

生成器和迭代器占内存的大小
'''

import os
import psutil

#显示 py程序 占用的内存大小

def show_memory(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    print(info)
    # print(info.__dict__)
    print(info.uss/1024/1024)

def test_container():
    show_memory('start -- test_container')
    list1 = [ i for i in range(100000000)]
    show_memory('after -- test_container')
    print(sum(list1))
    show_memory('afer some test_container')

def test_generator():
    show_memory('start -- test_generator')
    list1 = ( i for i in range(100000000))
    show_memory('after -- test_generator')
    print(sum(list1))
    show_memory('afer some test_generator')


test_container()
test_generator()