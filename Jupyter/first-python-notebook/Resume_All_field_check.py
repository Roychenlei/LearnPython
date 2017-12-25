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
resume = client['zippia_chenlei']['resume_5M']

i =0
A1Description = 0
A1Title = 0
A1Year = 0
A2Description = 0
A2Title = 0
A2Year = 0
A3Description = 0
A3Title = 0
A3Year = 0
A4Description = 0
A4Title = 0
A4Year = 0
A5Description = 0
A5Title = 0
A5Year = 0
AdditionalInformation = 0
City = 0
ContactName = 0
CoverLetterObjective = 0
CoverLetterParagraphs = 0
E1City = 0
E1Course = 0
E1DurationFrom = 0
E1DurationTo = 0
E1School_University = 0
E1State = 0
E2City = 0
E2Course = 0
E2DurationFrom = 0
E2DurationTo = 0
E2School_University = 0
E2State = 0
E3City = 0
E3Course = 0
E3DurationFrom = 0
E3DurationTo = 0
E3School_University = 0
E3State = 0
E4City = 0
E4Course = 0
E4DurationFrom = 0
E4DurationTo = 0
E4School_University = 0
E4State = 0
E5City = 0
E5Course = 0
E5DurationFrom = 0
E5DurationTo = 0
E5School_University = 0
E5State = 0
E6City = 0
E6Course = 0
E6DurationFrom = 0
E6DurationTo = 0
E6School_University = 0
E6State = 0
E7City = 0
E7Course = 0
E7DurationFrom = 0
E7DurationTo = 0
E7School_University = 0
E7State = 0
E8City = 0
E8Course = 0
E8DurationFrom = 0
E8DurationTo = 0
E8School_University = 0
E8State = 0
Link1 = 0
Link2 = 0
Link3 = 0
Link4 = 0
Link5 = 0
Link6 = 0
Link7 = 0
Link8 = 0
Skill = 0
SourceURL = 0
State = 0
StateVisaStatus = 0
W10City = 0
W10Description = 0
W10DurationFrom = 0
W10DurationTo = 0
W10Organization = 0
W10State = 0
W10Title = 0
W11City = 0
W11Description = 0
W11DurationFrom = 0
W11DurationTo = 0
W11Organization = 0
W11State = 0
W11Title = 0
W12City = 0
W12Description = 0
W12DurationFrom = 0
W12DurationTo = 0
W12Organization = 0
W12State = 0
W12Title = 0
W13City = 0
W13Description = 0
W13DurationFrom = 0
W13DurationTo = 0
W13Organization = 0
W13State = 0
W13Title = 0
W14City = 0
W14Description = 0
W14DurationFrom = 0
W14DurationTo = 0
W14Organization = 0
W14State = 0
W14Title = 0
W15City = 0
W15Description = 0
W15DurationFrom = 0
W15DurationTo = 0
W15Organization = 0
W15State = 0
W15Title = 0
W1City = 0
W1Description = 0
W1DurationFrom = 0
W1DurationTo = 0
W1Organization = 0
W1State = 0
W1Title = 0
W2City = 0
W2Description = 0
W2DurationFrom = 0
W2DurationTo = 0
W2Organization = 0
W2State = 0
W2Title = 0
W3City = 0
W3Description = 0
W3DurationFrom = 0
W3DurationTo = 0
W3Organization = 0
W3State = 0
W3Title = 0
W4City = 0
W4Description = 0
W4DurationFrom = 0
W4DurationTo = 0
W4Organization = 0
W4State = 0
W4Title = 0
W5City = 0
W5Description = 0
W5DurationFrom = 0
W5DurationTo = 0
W5Organization =   0
W5State = 0
W5Title = 0
W6City = 0
W6Description = 0
W6DurationFrom = 0
W6DurationTo = 0
W6Organization = 0
W6State = 0
W6Title = 0
W7City = 0
W7Description = 0
W7DurationFrom = 0
W7DurationTo = 0
W7Organization = 0
W7State = 0
W7Title = 0
W8City = 0
W8Description = 0
W8DurationFrom = 0
W8DurationTo = 0
W8Organization = 0
W8State = 0
W8Title = 0
W9City = 0
W9Description = 0
W9DurationFrom = 0
W9DurationTo = 0
W9Organization = 0
W9State = 0
W9Title = 0
for r in resume.find({}):
    i += 1
    if  r.get('A1Description') == '' :
     A1Description += 1 
    if  r.get('A1Title') == '' :
     A1Title += 1 
    if  r.get('A1Year') == '' :
     A1Year += 1 
    if  r.get('A2Description') == '' :
     A2Description += 1 
    if  r.get('A2Title') == '' :
     A2Title += 1 
    if  r.get('A2Year') == '' :
     A2Year += 1 
    if  r.get('A3Description') == '' :
     A3Description += 1 
    if  r.get('A3Title') == '' :
     A3Title += 1 
    if  r.get('A3Year') == '' :
     A3Year += 1 
    if  r.get('A4Description') == '' :
     A4Description += 1 
    if  r.get('A4Title') == '' :
     A4Title += 1 
    if  r.get('A4Year') == '' :
     A4Year += 1 
    if  r.get('A5Description') == '' :
     A5Description += 1 
    if  r.get('A5Title') == '' :
     A5Title += 1 
    if  r.get('A5Year') == '' :
     A5Year += 1 
    if  r.get('AdditionalInformation') == '' :
     AdditionalInformation += 1 
    if  r.get('City') == '' :
     City += 1 
    if  r.get('ContactName') == '' :
     ContactName += 1 
    if  r.get('CoverLetterObjective') == '' :
     CoverLetterObjective += 1 
    if  r.get('CoverLetterParagraphs') == '' :
     CoverLetterParagraphs += 1 
    if  r.get('E1City') == '' :
     E1City += 1 
    if  r.get('E1Course') == '' :
     E1Course += 1 
    if  r.get('E1DurationFrom') == '' :
     E1DurationFrom += 1 
    if  r.get('E1DurationTo') == '' :
     E1DurationTo += 1 
    if  r.get('E1School_University') == '' :
     E1School_University += 1 
    if  r.get('E1State') == '' :
     E1State += 1 
    if  r.get('E2City') == '' :
     E2City += 1 
    if  r.get('E2Course') == '' :
     E2Course += 1 
    if  r.get('E2DurationFrom') == '' :
     E2DurationFrom += 1 
    if  r.get('E2DurationTo') == '' :
     E2DurationTo += 1 
    if  r.get('E2School_University') == '' :
     E2School_University += 1 
    if  r.get('E2State') == '' :
     E2State += 1 
    if  r.get('E3City') == '' :
     E3City += 1 
    if  r.get('E3Course') == '' :
     E3Course += 1 
    if  r.get('E3DurationFrom') == '' :
     E3DurationFrom += 1 
    if  r.get('E3DurationTo') == '' :
     E3DurationTo += 1 
    if  r.get('E3School_University') == '' :
     E3School_University += 1 
    if  r.get('E3State') == '' :
     E3State += 1 
    if  r.get('E4City') == '' :
     E4City += 1 
    if  r.get('E4Course') == '' :
     E4Course += 1 
    if  r.get('E4DurationFrom') == '' :
     E4DurationFrom += 1 
    if r.get('E4DurationTo') == '' :
     E4DurationTo += 1 
    if r.get('E4School_University') == '' :
     E4School_University += 1 
    if r.get('E4State') == '' :
     E4State += 1 
    if r.get('E5City') == '' :
     E5City += 1 
    if r.get('E5Course') == '' :
     E5Course += 1 
    if  r.get('E5DurationFrom') == '' :
     E5DurationFrom += 1 
    if  r.get('E5DurationTo') == '' :
     E5DurationTo += 1 
    if  r.get('E5School_University') == '' :
     E5School_University += 1 
    if r.get(' E5State') == '' :
     E5State += 1 
    if r.get(' E6City') == '' :
     E6City += 1 
    if r.get(' E6Course') == '' :
     E6Course += 1 
    if  r.get('E6DurationFrom') == '' :
     E6DurationFrom += 1 
    if  r.get('E6DurationTo') == '' :
     E6DurationTo += 1 
    if  r.get('E6School_University') == '' :
     E6School_University += 1 
    if  r.get('E6State') == '' :
     E6State += 1 
    if  r.get('E7City') == '' :
     E7City += 1 
    if  r.get('E7Course') == '' :
     E7Course += 1 
    if  r.get('E7DurationFrom') == '' :
     E7DurationFrom += 1 
    if  r.get('E7DurationTo') == '' :
     E7DurationTo += 1 
    if  r.get('E7School_University') == '' :
     E7School_University += 1 
    if  r.get('E7State') == '' :
     E7State += 1 
    if  r.get('E8City') == '' :
     E8City += 1 
    if r.get(' E8Course') == '' :
     E8Course += 1 
    if r.get(' E8DurationFrom') == '' :
     E8DurationFrom += 1 
    if r.get(' E8DurationTo') == '' :
     E8DurationTo += 1 
    if r.get(' E8School_University') == '' :
     E8School_University += 1 
    if  r.get('E8State') == '' :
     E8State += 1 
    if  r.get('Link1') == '' :
     Link1 += 1 
    if  r.get('Link2') == '' :
     Link2 += 1 
    if  r.get('Link3') == '' :
     Link3 += 1 
    if  r.get('Link4') == '' :
     Link4 += 1 
    if  r.get('Link5') == '' :
     Link5 += 1 
    if  r.get('Link6') == '' :
     Link6 += 1 
    if  r.get('Link7') == '' :
     Link7 += 1 
    if  r.get('Link8') == '' :
     Link8 += 1 
    if  r.get('Skill') == '' :
     Skill += 1 
    if  r.get('SourceURL') == '' :
     SourceURL += 1 
    if  r.get('StateVisaStatus') == '' :
     StateVisaStatus += 1 
    if  r.get('W1City') == '' :
     W1City += 1 
    if  r.get('W1Description') == '' :
     W1Description += 1 
    if r.get('W1DurationFrom') == '' :
     W1DurationFrom += 1 
    if r.get('W1DurationTo') == '' :
     W1DurationTo += 1 
    if r.get('W1Organization') == '' :
     W1Organization += 1 
    if r.get('W1State') == '' :
     W1State += 1 
    if r.get('W1Title') == '' :
     W1Title += 1 
    if r.get('W11City') == '' :
     W11City += 1 
    if r.get('W11Description') == '' :
     W11Description += 1 
    if r.get('W11DurationFrom') == '' :
     W11DurationFrom += 1 
    if r.get('W11DurationTo') == '' :
     W11DurationTo += 1 
    if r.get('W11Organization') == '' :
     W11Organization += 1 
    if r.get('W11State') == '' :
     W11State += 1 
    if r.get('W11Title') == '' :
     W11Title += 1 
    if r.get('W12City') == '' :
     W12City += 1 
    if r.get('W12Description') == '' :
     W12Description += 1 
    if r.get('W12DurationFrom') == '' :
     W12DurationFrom += 1 
    if r.get('W12DurationTo') == '' :
     W12DurationTo += 1 
    if r.get('W12Organization') == '' :
     W12Organization += 1 
    if r.get('W12State') == '' :
     W12State += 1 
    if r.get('W12Title') == '' :
     W12Title += 1 
    if r.get('W13City') == '' :
     W13City += 1 
    if r.get('W13Description') == '' :
     W13Description += 1 
    if r.get('W13DurationFrom') == '' :
     W13DurationFrom += 1 
    if r.get('W13DurationTo') == '' :
     W13DurationTo += 1 
    if r.get('W13Organization') == '' :
     W13Organization += 1 
    if r.get('W13State') == '' :
     W13State += 1 
    if r.get('W13Title') == '' :
     W13Title += 1 
    if r.get('W14City') == '' :
     W14City += 1 
    if r.get('W14Description') == '' :
     W14Description += 1 
    if r.get('W14DurationFrom') == '' :
     W14DurationFrom += 1 
    if r.get('W14DurationTo') == '' :
     W14DurationTo += 1 
    if r.get('W14Organization') == '' :
     W14Organization += 1 
    if r.get('W14State') == '' :
     W14State += 1 
    if r.get('W14Title') == '' :
     W14Title += 1 
    if r.get('W15City') == '' :
     W15City += 1 
    if r.get('W15Description') == '' :
     W15Description += 1 
    if r.get('W15DurationFrom') == '' :
     W15DurationFrom += 1 
    if r.get('W15DurationTo') == '' :
     W15DurationTo += 1 
    if r.get('W15Organization') == '' :
     W15Organization += 1 
    if r.get('W15State') == '' :
     W15State += 1 
    if r.get('W15Title') == '' :
     W15Title += 1 
    if r.get('W1City') == '' :
     W1City += 1 
    if r.get('W1Description') == '' :
     W1Description += 1 
    if r.get('W1DurationFrom') == '' :
     W1DurationFrom += 1 
    if r.get('W1DurationTo') == '' :
     W1DurationTo += 1 
    if r.get('W1Organization') == '' :
     W1Organization += 1 
    if r.get('W1State') == '' :
     W1State += 1 
    if r.get('W1Title') == '' :
     W1Title += 1 
    if r.get('W2City') == '' :
     W2City += 1 
    if r.get('W2Description') == '' :
     W2Description += 1 
    if r.get('W2DurationFrom') == '' :
     W2DurationFrom += 1 
    if r.get('W2DurationTo') == '' :
     W2DurationTo += 1 
    if r.get('W2Organization') == '' :
     W2Organization += 1 
    if r.get('W2State') == '' :
     W2State += 1 
    if r.get('W2Title') == '' :
     W2Title += 1 
    if r.get('W3City') == '' :
     W3City += 1 
    if r.get('W3Description') == '' :
     W3Description += 1 
    if r.get('W3DurationFrom') == '' :
     W3DurationFrom += 1 
    if r.get('W3DurationTo') == '' :
     W3DurationTo += 1 
    if r.get('W3Organization') == '' :
     W3Organization += 1 
    if r.get('W3State') == '' :
     W3State += 1 
    if r.get('W3Title') == '' :
     W3Title += 1 
    if r.get('W4City') == '' :
     W4City += 1 
    if r.get('W4Description') == '' :
     W4Description += 1 
    if r.get('W4DurationFrom') == '' :
     W4DurationFrom += 1 
    if r.get('W4DurationTo') == '' :
     W4DurationTo += 1 
    if r.get('W4Organization') == '' :
     W4Organization += 1 
    if r.get('W4State') == '' :
     W4State += 1 
    if r.get('W4Title') == '' :
     W4Title += 1 
    if r.get('W5City') == '' :
     W5City += 1 
    if r.get('W5Description') == '' :
     W5Description += 1 
    if r.get('W5DurationFrom') == '' :
     W5DurationFrom += 1 
    if r.get('W5DurationTo') == '' :
     W5DurationTo += 1 
    if r.get('W5Organization') == '' :
     W5Organization += 1 
    if r.get('W5State') == '' :
     W5State += 1 
    if r.get('W5Title') == '' :
     W5Title += 1 
    if r.get('W6City') == '' :
     W6City += 1 
    if r.get('W6Description') == '' :
     W6Description += 1 
    if r.get('W6DurationFrom') == '' :
     W6DurationFrom += 1 
    if r.get('W6DurationTo') == '' :
     W6DurationTo += 1 
    if r.get('W6Organization') == '' :
     W6Organization += 1 
    if r.get('W6State') == '' :
     W6State += 1 
    if r.get('W6Title') == '' :
     W6Title += 1 
    if r.get('W7City') == '' :
     W7City += 1 
    if r.get('W7Description') == '' :
     W7Description += 1 
    if r.get('W7DurationFrom') == '' :
     W7DurationFrom += 1 
    if r.get('W7DurationTo') == '' :
     W7DurationTo += 1 
    if r.get('W7Organization') == '' :
     W7Organization += 1 
    if r.get('W7State') == '' :
     W7State += 1 
    if r.get('W7Title') == '' :
     W7Title += 1 
    if r.get('W8City') == '' :
     W8City += 1 
    if r.get('W8Description') == '' :
     W8Description += 1 
    if r.get('W8DurationFrom') == '' :
     W8DurationFrom += 1 
    if r.get('W8DurationTo') == '' :
     W8DurationTo += 1 
    if r.get('W8Organization') == '' :
     W8Organization += 1 
    if r.get('W8State') == '' :
     W8State += 1 
    if r.get('W8Title') == '' :
     W8Title += 1 
    if r.get('W9City') == '' :
     W9City += 1 
    if r.get('W9Description') == '' :
     W9Description += 1 
    if r.get('W9DurationFrom') == '' :
     W9DurationFrom += 1 
    if r.get('W9DurationTo') == '' :
     W9DurationTo += 1 
    if r.get('W9Organization') == '' :
     W9Organization += 1 
    if r.get('W9State') == '' :
     W9State += 1 
    if r.get('W9Title') == '' :
     W9Title += 1
    if i % 1000000 == 0:
     print i
print ('end')
print	('A1Description'),		A1Description
			
print	('A1Title'),		A1Title
			
print	('A1Year'),		A1Year
			
print	('A2Description'),		A2Description
			
print	('A2Title'),		A2Title
			
print	('A2Year'),		A2Year
			
print	('A3Description'),		A3Description
			
print	('A3Title'),		A3Title
			
print	('A3Year'),		A3Year
			
print	('A4Description'),		A4Description
			
print	('A4Title'),		A4Title
			
print	('A4Year'),		A4Year
			
print	('A5Description'),		A5Description
			
print	('A5Title'),		A5Title
			
print	('A5Year'),		A5Year
			
print	('AdditionalInformation'),		AdditionalInformation
			
print	('City'),		City
			
print	('ContactName'),		ContactName
			
print	('CoverLetterObjective'),		CoverLetterObjective
			
print	('CoverLetterParagraphs'),		CoverLetterParagraphs
			
print	('E1City'),		E1City
			
print	('E1Course'),		E1Course
			
print	('E1DurationFrom'),		E1DurationFrom
			
print	('E1DurationTo'),		E1DurationTo
			
print	('E1School_University'),		E1School_University
			
print	('E1State'),		E1State
			
print	('E2City'),		E2City
			
print	('E2Course'),		E2Course
			
print	('E2DurationFrom'),		E2DurationFrom
			
print	('E2DurationTo'),		E2DurationTo
			
print	('E2School_University'),		E2School_University
			
print	('E2State'),		E2State
			
print	('E3City'),		E3City
			
print	('E3Course'),		E3Course
			
print	('E3DurationFrom'),		E3DurationFrom
			
print	('E3DurationTo'),		E3DurationTo
			
print	('E3School_University'),		E3School_University
			
print	('E3State'),		E3State
			
print	('E4City'),		E4City
			
print	('E4Course'),		E4Course
			
print	('E4DurationFrom'),		E4DurationFrom
			
print	('E4DurationTo'),		E4DurationTo
			
print	('E4School_University'),		E4School_University
			
print	('E4State'),		E4State
			
print	('E5City'),		E5City
			
print	('E5Course'),		E5Course
			
print	('E5DurationFrom'),		E5DurationFrom
			
print	('E5DurationTo'),		E5DurationTo
			
print	('E5School_University'),		E5School_University
			
print	('E5State'),		E5State
			
print	('E6City'),		E6City
			
print	('E6Course'),		E6Course
			
print	('E6DurationFrom'),		E6DurationFrom
			
print	('E6DurationTo'),		E6DurationTo
			
print	('E6School_University'),		E6School_University
			
print	('E6State'),		E6State
			
print	('E7City'),		E7City
			
print	('E7Course'),		E7Course
			
print	('E7DurationFrom'),		E7DurationFrom
			
print	('E7DurationTo'),		E7DurationTo
			
print	('E7School_University'),		E7School_University
			
print	('E7State'),		E7State
			
print	('E8City'),		E8City
			
print	('E8Course'),		E8Course
			
print	('E8DurationFrom'),		E8DurationFrom
			
print	('E8DurationTo'),		E8DurationTo
			
print	('E8School_University'),		E8School_University
			
print	('E8State'),		E8State
			
print	('Link1'),		Link1
			
print	('Link2'),		Link2
			
print	('Link3'),		Link3
			
print	('Link4'),		Link4
			
print	('Link5'),		Link5
			
print	('Link6'),		Link6
			
print	('Link7'),		Link7
			
print	('Link8'),		Link8
			
print	('Skill'),		Skill
			
print	('SourceURL'),		SourceURL
			
print	('StateVisaStatus'),		StateVisaStatus
			
print	('W10City'),		W10City
			
print	('W10Description'),		W10Description
			
print	('W10DurationFrom'),		W10DurationFrom
			
print	('W10DurationTo'),		W10DurationTo
			
print	('W10Organization'),		W10Organization
			
print	('W10State'),		W10State
			
print	('W10Title'),		W10Title
			
print	('W11City'),		W11City
			
print	('W11Description'),		W11Description
			
print	('W11DurationFrom'),		W11DurationFrom
			
print	('W11DurationTo'),		W11DurationTo
			
print	('W11Organization'),		W11Organization
			
print	('W11State'),		W11State
			
print	('W11Title'),		W11Title
			
print	('W12City'),		W12City
			
print	('W12Description'),		W12Description
			
print	('W12DurationFrom'),		W12DurationFrom
			
print	('W12DurationTo'),		W12DurationTo
			
print	('W12Organization'),		W12Organization
			
print	('W12State'),		W12State
			
print	('W12Title'),		W12Title
			
print	('W13City'),		W13City
			
print	('W13Description'),		W13Description
			
print	('W13DurationFrom'),		W13DurationFrom
			
print	('W13DurationTo'),		W13DurationTo
			
print	('W13Organization'),		W13Organization
			
print	('W13State'),		W13State
			
print	('W13Title'),		W13Title
			
print	('W14City'),		W14City
			
print	('W14Description'),		W14Description
			
print	('W14DurationFrom'),		W14DurationFrom
			
print	('W14DurationTo'),		W14DurationTo
			
print	('W14Organization'),		W14Organization
			
print	('W14State'),		W14State
			
print	('W14Title'),		W14Title
			
print	('W15City'),		W15City
			
print	('W15Description'),		W15Description
			
print	('W15DurationFrom'),		W15DurationFrom
			
print	('W15DurationTo'),		W15DurationTo
			
print	('W15Organization'),		W15Organization
			
print	('W15State'),		W15State
			
print	('W15Title'),		W15Title
			
print	('W1City'),		W1City
			
print	('W1Description'),		W1Description
			
print	('W1DurationFrom'),		W1DurationFrom
			
print	('W1DurationTo'),		W1DurationTo
			
print	('W1Organization'),		W1Organization
			
print	('W1State'),		W1State
			
print	('W1Title'),		W1Title
			
print	('W2City'),		W2City
			
print	('W2Description'),		W2Description
			
print	('W2DurationFrom'),		W2DurationFrom
			
print	('W2DurationTo'),		W2DurationTo
			
print	('W2Organization'),		W2Organization
			
print	('W2State'),		W2State
			
print	('W2Title'),		W2Title
			
print	('W3City'),		W3City
			
print	('W3Description'),		W3Description
			
print	('W3DurationFrom'),		W3DurationFrom
			
print	('W3DurationTo'),		W3DurationTo
			
print	('W3Organization'),		W3Organization
			
print	('W3State'),		W3State
			
print	('W3Title'),		W3Title
			
print	('W4City'),		W4City
			
print	('W4Description'),		W4Description
			
print	('W4DurationFrom'),		W4DurationFrom
			
print	('W4DurationTo'),		W4DurationTo
			
print	('W4Organization'),		W4Organization
			
print	('W4State'),		W4State
			
print	('W4Title'),		W4Title
			
print	('W5City'),		W5City
			
print	('W5Description'),		W5Description
			
print	('W5DurationFrom'),		W5DurationFrom
			
print	('W5DurationTo'),		W5DurationTo
			
print	('W5Organization'),		W5Organization
			
print	('W5State'),		W5State
			
print	('W5Title'),		W5Title
			
print	('W6City'),		W6City
			
print	('W6Description'),		W6Description
			
print	('W6DurationFrom'),		W6DurationFrom
			
print	('W6DurationTo'),		W6DurationTo
			
print	('W6Organization'),		W6Organization
			
print	('W6State'),		W6State
			
print	('W6Title'),		W6Title
			
print	('W7City'),		W7City
			
print	('W7Description'),		W7Description
			
print	('W7DurationFrom'),		W7DurationFrom
			
print	('W7DurationTo'),		W7DurationTo
			
print	('W7Organization'),		W7Organization
			
print	('W7State'),		W7State
			
print	('W7Title'),		W7Title
			
print	('W8City'),		W8City
			
print	('W8Description'),		W8Description
			
print	('W8DurationFrom'),		W8DurationFrom
			
print	('W8DurationTo'),		W8DurationTo
			
print	('W8Organization'),		W8Organization
			
print	('W8State'),		W8State
			
print	('W8Title'),		W8Title
			
print	('W9City'),		W9City
			
print	('W9Description'),		W9Description
			
print	('W9DurationFrom'),		W9DurationFrom
			
print	('W9DurationTo'),		W9DurationTo
			
print	('W9Organization'),		W9Organization
			
print	('W9State'),		W9State
			
print	('W9Title'),		W9Title