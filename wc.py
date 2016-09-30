#!/usr/bin/env python
import sys

"""
A simple/test python program similar to the unix wc command
"""

with open(sys.argv[1]) as testfile:
	linecount = 0
	wordcount = 0
	charcount = 0
	for line in testfile:
		linecount += 1
		# count how many words each line
		words = line.split()
		wordcount += len(words)
		for word in words:
			# different than wc, do not count space
			charcount += len(word)
	print("lines: " + str(linecount) + " words: " + str(wordcount) + \
		" chars: " + str(charcount) + "\n")
