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


