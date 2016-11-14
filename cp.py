#!/usr/bin/env python
import sys

"""
A simple/test python program similar to the unix cp command
"""
if len(sys.argv) != 3:
	print("need from and to file names.\n")
else:
	try:
	    with open(sys.argv[1]) as fromfile:
	    	with open(sys.argv[2], 'w') as tofile:
			for line in fromfile:
				tofile.write(line)
	except IOError:
	    print("IO Error\n")
