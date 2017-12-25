import pymongo
from pymongo import MongoClient
from collections import Counter

client = MongoClient(host='localhost')
resume_old = client['zippia_pipeline']['resume']

i = 0
City = []
for r in resume_old.find({}):
	i += 1
	City.append(r.get('City'))
	if i %1000000 ==0:
		print (i)

City_count = Counter(City)

for key,value in sorted(City_count.items(), key=lambda item: (item[1],item[0]),reverse = True):
	print ("%s: %s" % (key, value))


