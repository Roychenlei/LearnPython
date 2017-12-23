# -*- coding: utf-8 -*-

# sum = lambda arg1, arg2: arg1+arg2

# print "Value of total :",sum(20,10)

# def make_incrementor(n): 
# 	return lambda x: x+n

# print "Function Value of total :",make_incrementor(22)(33)

def f1(a, b, c=0, *args, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)



f1(1,2)

