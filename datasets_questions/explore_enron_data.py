#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pprint 

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

pprint.pprint(enron_data)
print len(enron_data.items())
print len(enron_data.values()[0])
print 'Person\'s of interest ' + str(sum([1 for k in enron_data.keys() if enron_data[k]['poi'] == True ]))
pprint.pprint(enron_data['PRENTICE JAMES'])
pprint.pprint(enron_data['COLWELL WESLEY'])
pprint.pprint(enron_data.keys())
pprint.pprint(enron_data["SKILLING JEFFREY K"])
pprint.pprint(enron_data["LAY KENNETH L"])
pprint.pprint(enron_data["FASTOW ANDREW S"])

count1 = 0
count2 = 0

for k in enron_data:
  if enron_data[k]['salary'] != 'NaN':
    count1 += 1
  if enron_data[k]['email_address'] != 'NaN':
    count2 += 1
print 'Quantifiable Salary : ' + str(count1)
print 'Known Mail Adresses : ' + str(count2)
print sum([1 for k in enron_data.keys() if enron_data[k]['total_payments'] == "NaN" and enron_data[k]['poi'] == True])
print sum([1 for k in enron_data.keys() if enron_data[k]['total_payments'] == "NaN" and enron_data[k]['poi'] == True])/float(len(enron_data.items()))
