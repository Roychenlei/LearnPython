import pymongo
from pymongo import MongoClient
from collections import Counter

client = MongoClient(host='localhost')
resume_old = client['zippia_pipeline']['resume']

i = 0
State = []
for r in resume_old.find({}):
	i += 1
	State.append(r.get('State'))
	if i %1000000 ==0:
		print (i)

State_count = Counter(State)

for key,value in sorted(State_count.items(), key=lambda item: (item[1],item[0]),reverse = True):
	print ("%s: %s" % (key, value))


