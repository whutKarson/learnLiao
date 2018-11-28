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

"""
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
"""
def str2float(s):
	"""
	大概思路，先找寻s里头是否有"."并确定index，
	利用map把对应的s转换成为数字
	利用reduce把对应的数字变成一个number总和
	"""
	 # 先创建一个digit 字符数字对应表
	DIGITS = {
	 	'0': 0, 
	 	'1': 1,
	 	'2': 2,
	 	'3': 3,
	 	'4': 4,
	 	'5': 5,
	 	'6': 6,
	 	'7': 7,
	 	'8': 8,
	 	'9': 9
	}

	index_of_dot = s.index('.')

	right, left = map(lambda x: DIGITS[x], s[:index_of_dot]), map(lambda x: DIGITS[x], s[index_of_dot+1:])
	#print(f"right: {right} , left: {left}")

	sum_right = reduce(lambda x,y: x*10 + y, right)
	"""
	n = 0
	sum_left = 0
	for i in left:
		sum_left += i * (0.1 ** (n + 1))
		n += 1
	"""
	"""
	第二种思路去处理 右边的小数点部分
	比如说left现在等于 [4,5,6],
	先把它拼接成数字456， 然后乘以对应的list的长度0.1的阶乘
	"""
	sum_left = reduce(lambda x, y: x*10 + y, left) * 0.1 ** len(s[index_of_dot+1:])

	return sum_left + sum_right



print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

