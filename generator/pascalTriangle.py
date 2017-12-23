#!/user/bin/env python
#coding: 'utf-8'

def triangles():
	N = [1]
	while True:
		yield N
		N.append(0)
		N = [N[i]+N[i-1] for i in range(len(N))]


if __name__ == '__main__':
	n = 0
	for t in triangles():
		print (t)
		n = n+1
		if n == 5:
			break