from functools import wraps
def hello(fn):
	@wraps(fn)
	def wrapperx():
		print ("hello, %s"% fn.__name__)
		fn()
		print ("goodbye, %s" % fn.__name__)
	return wrapperx

@hello
def foo():
	print "i am foo"
	pass

foo()
print foo.__name__
print foo.__doc__