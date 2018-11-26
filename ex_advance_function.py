# -*- coding: utf-8 -*-

from functools import reduce

"""
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

"""

def f(x):
	return x * x

r = map(f, [1, 2, 4, 5, 6])

print(list(r))
# 期望输出为 [1, 4, 16, 25, 36]


"""
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

"""

def add(x, y):
	return x + y

r_add = reduce(add, [1, 2, 4, 5, 6])
print(r_add)

# 期望输出 18


"""
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
"""
def normalize(name):
    return name[:1].upper() + name[1:].lower()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

"""
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
"""

def prod(L):
    return reduce(lambda x, y: x * y, L)

# 测试:
L3 = [1, 2, 3, 4, 5, 6]
L4 = [0, 1, 2, 3, 4]
L5 = [-1, -2, -3]
r_prod_L3 = prod(L3)
r_prod_L4 = prod(L4)
r_prod_L5 = prod(L5)
print(r_prod_L3)
print(r_prod_L4)
print(r_prod_L5)

