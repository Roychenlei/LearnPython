import pymongo
from pymongo import MongoClient
from collections import Counter

client = MongoClient(host='192.168.1.201')
resume = client['zippia_chenlei']['resume_5M']

i = 0
W1Title = []
for r in resume.find({}):
	i += 1
	W1Title.append(r.get('W1Title'))
	if i %1000000 ==0:
		print (i)

W1Title_count = Counter(W1Title)

for key,value in sorted(W1Title_count.items(), key=lambda item: (item[1],item[0]),reverse = True):
	print ("%s: %s" % (key, value))


