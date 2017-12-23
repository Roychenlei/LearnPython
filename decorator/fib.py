# from functools import lru_cache

fibonacci_cache = {}

def fibonacci(n):
	# If we have cached the value, then return it
	if n in fibonacci_cache:
		return fibonacci_cache[n]

	# Compute the Nth term
	if n == 1:
		value = 1
	elif n== 2:
		value = 1
	elif n > 2 :
		value = fibonacci(n-1) + fibonacci(n-2)

	# Cache the value and return it
	fibonacci_cache[n] = value

	return value




def fibonacci_opt(n):
	# cheeck that the input is a positive integer
	if type(n) != int:
		raise TypeError("n must be positive int")
	if n < 1:
		raise ValueError("n must be a positive int")
	# Compute the Nth term
	if n == 1:
		return 1
	elif n ==2:
		return 1
	elif n > 2:
		return fibonacci_opt(n-1) + fibonacci_opt(n-2)

# for n in range(1, 41):
# 	print(n,fibonacci_opt(n))

for n in range(1,1000):
	print(n, fibonacci(n))
