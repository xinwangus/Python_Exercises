#!/usr/bin/env python
import sys
from math import log

"""
Experiment with IR (Information Retrival) technology, tf-idf
(Term Frequency, Inverse Document Frequency)
"""

# return a normalized "term frequency"
def tf(term, doc):
	# split the document and clean up
	words = [word.rstrip(',.') for word in doc.lower().split()]
	length = len(words)
	ct = words.count(term.lower())
	return float(ct/float(length))

def idf(term, doclist):
	
	

testdoc = "This is a test document with some words, and phrases."
term = "test"

print("tf score for " + term + " is: " + \
			str(tf(term, testdoc)) + "\n")
