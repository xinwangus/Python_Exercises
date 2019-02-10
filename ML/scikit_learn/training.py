''' 
experiment with plot csv data, and use scikit-learn
'''
import logging
import seaborn as sns
import csv
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier

if __name__ == '__main__':
    ''' Read CSV as Pandas df'''
    logging.basicConfig(level=logging.DEBUG,\
        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.disable(logging.DEBUG)
    # data_csv is pandas data frame type
    data_csv = pd.read_csv('data.csv')

    ''' Plot Pandas df'''
    sns.set()
    #sns.barplot(x=data_csv.type, y= data_csv.D)
    #sns.jointplot(x="type", y="A", data=data_csv)
    sns.pairplot(data=data_csv, hue="type")

    ''' Pandas df to Python data and Numpy data'''
    original_headers = list(data_csv.columns.values)
    logging.debug(original_headers)

    # pandas data into numpy array and pick columns
    numpy_array = data_csv.values
    logging.debug((type(numpy_array)))
    #logging.debug(numpy_array)
    features = numpy_array[:, 1:] # select columns 1 through end
    target = numpy_array[:, 0] # select colume 0, which is type, our target
    #print(features)

    ''' Scikit-learn: split, train. predict, and evaluate'''
    X_train, X_test, y_train, y_test = \
        train_test_split(features, target, test_size=0.4)
    #print(X_train)
    logging.debug(X_train.shape)

    # KNC model
    knc = KNeighborsClassifier(n_neighbors=3)
    knc.fit(X_train, y_train)
    y_predict = knc.predict(X_test)
    logging.debug(metrics.accuracy_score(y_test, y_predict))




