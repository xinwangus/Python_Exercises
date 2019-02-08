#!/usr/bin/env python
import sys
from pdb import set_trace

'''
A simple/test python program similar to the unix wc command.
'''
def wc(file):
    try:
        with open(file) as testfile:
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
                
        print('\t'+ str(linecount), \
              str(wordcount), \
              str(charcount), \
              file, sep='\t')
    except IOError:
        print("File \"" + file + "\" not found!")

if __name__ == '__main__':
	set_trace()   
	if len(sys.argv) != 2:
    		print("need a file name.\n")
	else:
    		wc(sys.argv[1])
