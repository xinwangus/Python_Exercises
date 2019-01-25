#!/usr/bin/env python
# coding: utf-8

# # Name-Value to CSV
# This is to transform the sparse/raw data in the format of 
#    Name Value
# to CSV format.
# 
# Each raw data file contains data for just one row in the CSV file.

# In[37]:


get_ipython().system('ls -al data')


# In[5]:


get_ipython().system('cat data/type_one_linux_1 ')


# In[6]:


get_ipython().system('cat data/type_two_linux_1')


# In[7]:


import csv
import logging
import os

logging.basicConfig(level=logging.DEBUG,                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

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
        dic_row[key] = int(value*100/sum_v)     
    logging.debug(dic_row)
    return dic_row
    
logging.debug('Start of program')    
with open('data.csv', 'w', newline='') as csvfile:
#    fields = ['type',\
#              'A', 'B', 'C', 'D', 'E','F','G', \
#              'H', 'I', 'J', 'K', 'L', 'M', 'N', \
#             'O', 'P', 'Q', 'R', 'S', 'T', \
#              'U', 'V', 'W', 'X', 'Y', 'Z']
    fields = ['type',              'A', 'B', 'C', 'D']
    dic_writer = csv.DictWriter(csvfile, fieldnames=fields)
    dic_writer.writeheader()
    for filename in os.listdir('data'):
        # dictionary writer is very nice to write
        # the values at the correct CSV spots
        dic_writer.writerow(build_row('data/' + filename)) 
logging.debug('End of program')  


# In[8]:


get_ipython().system('cat ./data.csv')


# # Play with Seaborn and Pandas

# In[55]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


import seaborn as sns
import pandas as pd

sns.set()

data_csv = pd.read_csv('data.csv')
#logging.debug(type(data_csv))

#sns.barplot(x=data_csv.type, y= data_csv.D)
#sns.jointplot(x="type", y="A", data=data_csv)

sns.pairplot(data=data_csv, hue="type")


# In[ ]:




