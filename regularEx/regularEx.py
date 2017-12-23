#!/usr/bin/python
#coding=utf8
import re,urllib
try:
	import urllib.request
except:
	pass

sits = 'google bbc cnn msn django'.split()
pat = re.compile(r'<title>+.*</title>+',re.I|re.M)

for s in sits:
	print ('Searching:'+s)
	try:
		u = urllib.urlopen('http://' + s +'.com')
	except:
		u = urllib.request.urlopen('http://' + s + '.com' )
	text = u.read()
	title = re.findall(pat,str(text))
	print(title[0])










#print (re.split(r'[a-f]','wesdsdsFSEEFGHNELJ;aaaaaasdlsddhhlsdswew,k',re.I|re.M))