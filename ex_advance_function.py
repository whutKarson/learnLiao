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


"""
回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
"""
def is_palindrome(n):

	# option 1
    """
    思路： 先把一个数按照位数从低到高 组成一个list，然后再按照list重新组成一个新的数字，位数不变，但是最高位变成最低位，最低位变成最高位，从低到高
    比较新的数字和原来的数字的大小，如果相等，则返回True
    """
    """
    # 创建一个list， 用于存储拆分后的数字
    L = []
    # 创建一个临时变量，值和n相等
    temp = n
    # 创建一个计数器，用来结束循环
    counter = 1
    while counter >= 1:    # 如果计数器 大于等于1， 那就意味着temp还为两位数或1位整数
    	counter = temp / 10    # 不断除以 10， 用来给temp降阶
    	#print(f"counter: {counter}")
    	L.append(temp % 10)    # list存储拆分后的数字
    	temp = temp // 10    # 临时变量 temp不断以10为阶乘降位
    #print(L)
    r = reduce(lambda x, y: x*10 + y, L)    # 重新组合， 位数不变，按照原来的低-->高位排列
    #print(f"r: {r} true or false: {r==n}")
    return (r == n)    # 比较新的组合数字和原来传入的数字

    """
    # option 2
    """
    利用str的切片原理
    """
    return str(n) == str(n)[::-1]


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))

if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

"""
计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：

首先，列出从2开始的所有自然数，构造一个序列：

2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：

3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：

5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数5，然后用5把序列的5的倍数筛掉：

7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

不断筛下去，就可以得到所有的素数。
"""
# 生成器，构造一个从3 开始的序列，并且是一个无限序列
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

# 再定义一个筛选函数, 筛选出对应的n的倍数
def _not_divisable(n):
	return lambda x: x%n > 0

# 再定义一个生成器，不断的返回下个素数
def primes():
	yield 2
	it = _odd_iter() # 初始序列
	while True:
		n = next(it) # 返回it的第一个元素
		yield n # 每次调用primes的next方法时 ，都返回n值
		it = filter(_not_divisable(n), it) # 重新构建it序列，利用filter方法，排除掉n的倍数

for n in primes():
	if n < 1000:
	    print(n)
	else:
		break




