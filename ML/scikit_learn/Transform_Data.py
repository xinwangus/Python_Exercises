#!/usr/bin/env python
# coding: utf-8

# # Name-Value to CSV
# This is to transform the sparse/raw data in the format of 
#    Name Value
# to CSV format.
# 
# Each raw data file contains data for just one row in the CSV file.

import csv
import logging
import os

logging.basicConfig(level=logging.DEBUG,\
                    format='%(asctime)s - %(levelname)s - %(message)s')
# If want:
#logging.disable(logging.DEBUG)

def decide_type(file_name):
    if file_name.find('one') != -1:
        return 1
    elif file_name.find('two') != -1:
        return 2
    else:
        return 0
    
# build an dictionary to represent a row in csv file.
def build_row(file_name):
    dic_row = {}
    # holds data before they are normalized
    dic_row_raw = {}
    
    dic_row['type'] = decide_type(file_name)
    logging.debug("type of file " + file_name + " is " + str(dic_row['type']))
    
    with open(file_name, 'r') as df:
        for row in df:
            words = row.split()
            # assert len is 2
            assert len(words) == 2, 'raw data row format wrong!'
            dic_row_raw[words[0]] = int(words[1])
    # Now we need to normalize data to percentage
    sum_v = 0
    for key, value in dic_row_raw.items():
        sum_v += value
    # adding order does not matter
    for key, value in dic_row_raw.items():
        dic_row[key] = round(value*100/sum_v)     
    logging.debug(dic_row)
    return dic_row
    
if __name__ == '__main__':
    logging.debug('Start of program')    
    with open('data.csv', 'w', newline='') as csvfile:
        fields = ['type','A', 'B', 'C', 'D']
        dic_writer = csv.DictWriter(csvfile, fieldnames=fields)
        dic_writer.writeheader()
        for filename in os.listdir('data'):
            # dictionary writer is very nice to write
            # the values at the correct CSV spots
            dic_writer.writerow(build_row('data/' + filename)) 
    logging.debug('End of program')  



import seaborn as sns
import pandas as pd

sns.set()

data_csv = pd.read_csv('data.csv')
#logging.debug(type(data_csv))

#sns.barplot(x=data_csv.type, y= data_csv.D)
#sns.jointplot(x="type", y="A", data=data_csv)

sns.pairplot(data=data_csv, hue="type")


# # Feed data to scikit learn

# In[83]:


# Try to feed the data in data.csv to sci-kit learn
import numpy as np
import pandas as pd
import logging

from sklearn import metrics

logging.basicConfig(level=logging.DEBUG,                    format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)

#
# ----- Step one: read data into Pandas
#
data_csv = pd.read_csv('data.csv')
#logging.debug((type(data_csv)))
original_headers = list(data_csv.columns.values)
#logging.debug(original_headers)
data_csv = data_csv._get_numeric_data()
# logging.debug((type(data_csv)))

#
# ----- Step two: data into numpy array and pick columns
#
numpy_array = data_csv.values
#logging.debug((type(numpy_array)))
#logging.debug(numpy_array)
features = numpy_array[:, 1:] # select columns 1 through end
target = numpy_array[:, 0] # select colume 0, which is type, our target
#logging.debug((type(features)))
#logging.debug(features)
#logging.debug((type(target)))
logging.debug(target)
#logging.debug(features.shape)
#logging.debug(target.shape)

#
# ----- Step three: feed into Scikit learn, fit and predict
#

X_new = [[15, 12, 17, 56], [31, 31, 18, 18]]
y_new = [2, 1]

# No. 1, OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
classif = OneVsRestClassifier(estimator=SVC(gamma='scale', random_state=0))
#logging.debug(classif)
classif.fit(features, target)
#logging.debug(classif.predict(X_new))
# gives array([2, 1]), which is correct
y_predict = classif.predict(features)
#logging.debug(y_predict)
#Following is training accuracy
logging.debug(metrics.accuracy_score(target, y_predict))

# No. 2, K neighbors
from sklearn.neighbors import KNeighborsClassifier
knc = KNeighborsClassifier(n_neighbors=3)
#logging.debug(knc)
knc.fit(features, target)
#logging.debug(knc.predict(X_new))
# gives array([2, 1]), which is correct. 
y_predict = knc.predict(features)
#logging.debug(y_predict)
#Following is training accuracy
logging.debug(metrics.accuracy_score(target, y_predict))

# No. 3, LogisticRegression (actaully a classifier)
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(features, target)
#logging.debug(logreg.predict(X_new))
# gives array([2, 1]), which is correct.
y_predict = logreg.predict(features)
#logging.debug(y_predict)
#Following is training accuracy
logging.debug(metrics.accuracy_score(target, y_predict))


# # Split data into training and testing Sets

# In[86]:


import numpy as np
import pandas as pd
import logging

from sklearn import metrics

logging.basicConfig(level=logging.DEBUG,                    format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)

#
# ----- Step one: read data into Pandas
#
data_csv = pd.read_csv('data.csv')
#logging.debug((type(data_csv)))
original_headers = list(data_csv.columns.values)
#logging.debug(original_headers)
data_csv = data_csv._get_numeric_data()
# logging.debug((type(data_csv)))

#
# ----- Step two: data into numpy array and pick columns
#
numpy_array = data_csv.values
#logging.debug((type(numpy_array)))
#logging.debug(numpy_array)
features = numpy_array[:, 1:] # select columns 1 through end
target = numpy_array[:, 0] # select colume 0, which is type, our target
#logging.debug((type(features)))
#logging.debug(features)
#logging.debug((type(target)))
#logging.debug(target)
#logging.debug(features.shape)
#logging.debug(target.shape)
print(features)

from sklearn.model_selection import train_test_split 

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.4)
print(X_train)
print(X_train.shape)


#logging.debug(target)
#logging.debug(features.shape)
#logging.debug(target.shape)


# In[ ]:




