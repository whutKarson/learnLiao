# -*- coding: utf-8 -*-


def findMinAndMax(L):
    """

    """
    if len(L) > 0:

        max = L[0]    # 初始化max值，赋值为第一个item值
        min = L[0]    # 初始化min值，赋值为第一个item值

        for i in L:    # 遍历list L，获取每个item的值
            if max < i:    # 判断max值和 i值的大小，如果max比i值小
        	    max = i    # 把i值赋值给max
            elif min > i:    # 如果max值大于i，再来判断min值是否大于i， 如果大于i
        	    min = i    # 把i值赋于给min

        print(min, max)
        return(min, max)

    return (None, None)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
elif findMinAndMax(['a', 'c', 'g', 'e', 'q']) != ('a', 'q'):
	print("测试失败！")
else:
    print('测试成功!')