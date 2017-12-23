import logging
logging.basicConfig(level=logging.INFO)


def foo(s):
	s = '0'
	n = int(s)
	# assert n !=0, 'n is zero'
	logging.info('n = %d' %n)
	print(10 / n)
	return 10 / n
def main():
	foo('0')
main()