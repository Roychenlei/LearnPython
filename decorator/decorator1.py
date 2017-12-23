def hello(fn):
	def wrapper():
		print "hello, %s" % fn.__name__
		fn()
		print "goodby, %s" % fn.__name__
	return wrapper

@hello
def foo():
	print "i am foo "

foo()


print '###########'


def fuck(fn):
	print "fuck %s" % fn.__name__[::-1].upper()


@fuck
def wfg():
	pass