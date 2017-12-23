def is_palindrome(n):
	L = list(str(n))
	while((len(L)>1) and (L[0] == L[-1])):
		L.pop(0)
		L.pop()
	if(len(L)<2):
		return n



result = list(filter(is_palindrome,range(1,100)))
print result