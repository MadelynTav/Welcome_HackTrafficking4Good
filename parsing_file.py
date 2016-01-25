import pandas
import json
from pandas.io.json import json_normalize
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pandas.read_csv('rubmapscsv.csv')
reviews = data['reviews']

allParlors = data['Name']

print allParlors
locationDict = {"one": 1}

for location in allParlors:

	if locationDict.has_key(location):
			num = locationDict.get(location)
			num+=1
			locationDict[location] = num;
	else:
		locationDict[location] = 1;

#plt.bar(range(len(locationDict)), locationDict.values(), align='center')
#plt.xticks(range(len(locationDict)), locationDict.keys(), rotation=25)
#for key, value in sorted(locationDict.iteritems(), key=lambda (k,v): (v,k)):
 #   print "%s: %s" % (key, value)




print(len(reviews))

dict = {'new':2};

print dict['new']

for review in reviews:
	x = pandas.read_json(review)
	if 'user' in x: 
		my_list = x['user']
		for person in my_list:
			if dict.has_key(person):
				num = dict.get(person)
				num+=1
				dict[person] = num;
	else:
		dict[person] = 1;

for key, value in sorted(dict.iteritems(), key=lambda (k,v): (v,k)):
    print "%s: %s" % (key, value)

#dict_two = sorted(dict, key=dict.get, reverse=True)
#print dict_two

# parsed_reviews_two = reviews[5]


# print (reviews)

# parsed_reviews = pandas.read_json(data['reviews'][0])

# print (len(parsed_reviews))
# print(parsed_reviews["user"])

 #massTime = data[data['State'] == 'Massachusetts']['reviews']


# print from_json
# reviews = data['reviews']