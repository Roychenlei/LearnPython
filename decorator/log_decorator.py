def log(func):
	def wrapper(*args, **kw):
		print'call %s():' %func.__name__
		return func(*args,**kw)
	return wrapper

@log
def now(param):
	print ('hello:$s' %param)
	print'2017-23-23'

now('ss')