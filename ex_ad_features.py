# -*- coding: utf-8 -*-
"""
利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
"""


def trim(s):
	"""
	# option1
	tmp = s[:]    # 复制一个string，结果不影响原来传入的参数
	print(tmp)    # print out 复制的string
	while True:    # 创建一个循环列表，不断check更新后的string的首位是否还有‘ ’，如果有，继续处理
		if len(tmp) > 0: # 判断tmp是否为空，如果为空，则强行中断循环，并返回空值
			start = tmp[0] # 获取首字母
			#print(f"start {start}")
			last = tmp[-1] # 获取末字母
			#print(f"last: {last}")
			if start != ' ' and last != ' ': # 如果首尾字母都不为空，中断循环，并返回更新后的tmp
				#print(f"tmp: _{tmp}_")
				return tmp
			if start == ' ':    # 如果首字母为空，利用slice特性截取 并让tmp变量指向新的str
				tmp = tmp[1:]
			if last == ' ':    # 如果末字母为空，利用slice特性截取 并让tmp变量指向新的str
				tmp = tmp[:-1]
		else:    # 如果为tmp为空，则强行中断循环，并返回空值
			#print(f"tmp _{tmp}_")
			return tmp
	"""
	# option2 类似于冒泡排序，遍历整个str list，如果前头或者后头为空，初始游标往后挪一位，末尾游标往前挪一位

	"""
	start = 0    # 首游标起始值
	end = len(s) - 1 # 末尾游标初始值

	for i in range(end):    # 此处for 循环的end值已经固定，for循环内部的end值更改不影响该循环值
		print(f"end: before: {end}")   # 输出end值
		if s[start] == ' ':    # 判断首游标处str字母值是否为空，如为空，首游标值+1
			start += 1
			print(f"after start {start}")
		if s[end] == ' ':   # 判断首游标处str字母值是否为空，如为空，末游标值-1
			end -= 1
			print(f"after end {end}")
	return s[start:end + 1]   #返回依据首末游标处str
	"""
	# option3 和option2一样的算法，只是代码上更加简洁一些，而且实现方式上程序负担也没那么重？依赖于切片操作所需要耗费的资源数
	while s[0:1] == ' ':    # 获取首个index处是否为空格值
		s = s[1:]    # 如果首字母为空格值，切片，并重新赋值s

	while s[-1:] == ' ':     # 获取末尾index处是否为空格值
		s = s[:-1]     # 如果末尾字母为空格值，切片，并重新赋值s

	print(s)
	return s 


# 测试

if trim("hello ") != "hello":
	print("测试失败")
elif trim(' hello') != "hello":
	print("failed!")
elif trim(' hello ') != 'hello':
	print('failed!')
elif trim('    ') != '':
	print('failed!')
elif trim('') != '':
	print('failed!')
else:
	print('Pass!')

