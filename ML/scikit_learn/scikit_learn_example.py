#!/usr/bin/env python
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier

# Training data
# assume each element is percentages of [Read, Write, Meta Op]
X = [[60, 10, 30], [61, 11, 28], [20, 10, 70], [10, 80, 10], [59, 12, 29]]
# something around [60, 10, 30] is, say database work load.
y = [1, 1, 0, 0, 1]

classif = OneVsRestClassifier(estimator=SVC(gamma='scale', random_state=0))
classif.fit(X, y)

# Prediction
print(classif.predict([[55, 11, 34], [0, 0, 100]]))
# this gives array([1, 0]), which is correct. 


