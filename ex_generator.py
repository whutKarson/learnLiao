# -*- coding: utf-8 -*-

def triangles():

	L = [1]

	while True:
		yield L
		for i in range(1, len(L)):
			L[i] = pre[i] + pre[i-1]
		L.append(1)
		pre = L[:]


tria = triangles()
n = 0
for l in tria:

	print(l)
	n += 1
	if n > 10:
		break



