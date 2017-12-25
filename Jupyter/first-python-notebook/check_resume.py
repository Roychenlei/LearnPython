from pymongo import MongoClient
import pandas as pd
import numpy as np
import pymongo
import pickle
import json
import time
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(color_codes=True)
FILE = "/home/liu/Downloads/resume_1m.csv"

client = MongoClient(host='192.168.1.201')
client1 = MongoClient(host='mongodb1.dev.zippia.com')
resume = client['zippia_chenlei']['resume_5M']
resume_old = client1['zippia_pipeline']['resume']

i = 0
SourceURL = []
State = []
City = []
W1Title = []
for r in resume.find({}):
    i += 1
    SourceURL.append(r.get('SourceURL'))
    State.append(r.get('State'))
    City.append(r.get('City'))
    W1Title.append(r.get('W1Title'))
    if i % 1000000 ==0:
        print (i)


from collections import Counter
City_count = Counter(City)
State_count = Counter(State)
W1Title_count = Counter(W1Title)


for key,value in sorted(City_count.items(), key=lambda item: (item[1],item[0]),reverse = True):
    print ("%s: %s" % (key, value))
