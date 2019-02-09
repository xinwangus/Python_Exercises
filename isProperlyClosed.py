#!/usr/bin/env python3

# A test program to check if a string containing
# [] {} () are properly closed, and no interlace
# Very similiar to the C++ version I wrote, but use
# python list to simulate a "stack"

def isClosed (s):
	nextToClose = []
	my_dict = {'[':']', '{':'}', '(':')'}
	left_b = my_dict.keys()
	right_b = my_dict.values()
	for c in s:
		if c in left_b:
			nextToClose.append(c)
		elif c in right_b:
			# List already empty
			if (len(nextToClose) == 0):
				return False
			else:
				assert nextToClose[-1] in left_b
			# close does not match open
			if (c != my_dict[nextToClose[-1]]):
				return False
			else:   
				nextToClose.pop()	
	if len(nextToClose) != 0:
		return False
	else:
		return True

if __name__ == '__main__':
	while True:
		ss = input("String to check:")
		if isClosed(ss):
			print (ss + " is Properly Closed, Good Job!")
		else:
			print (ss + " is not Properly Closed!")
		
