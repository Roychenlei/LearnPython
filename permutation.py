#!/user/bin/env python
#coding: 'utf-8'
import time
perm_lst = []
count =1

def permutation(lst):

	if  lst == []:
		print "result:",perm_lst
	else:

		for elem in lst:
			# print "perm_list3",perm_lst
			perm_lst.append(elem)
			rest_lst = lst[:]
			rest_lst.remove(elem)
			# print "================="
			print "perm_list1",perm_lst
			print "rest_list:",rest_lst
			# print "count",count 
			# print "================="
			permutation(rest_lst)
			# time.sleep(20)
			perm_lst.pop()
			print "perm_list2",perm_lst
			#print "perm_list3",perm_lst
			# global count
			# count +=1

if __name__ == '__main__':
	permutation(list('abc'))