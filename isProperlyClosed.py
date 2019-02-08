#!/usr/bin/env python3

# A test program to check if a string containing
# [] {} () are properly closed, and no interlace
# Very similiar to the C++ version I wrote, but use
# python list to simulate a "stack"

def isClosed (s):
	i = 0
	nextToClose = []
	my_dict = {'[':']', '{':'}', '(':')'}
	left_b = my_dict.keys()
	right_b = my_dict.values()
	while i < len(s):
		if s[i] in left_b:
			nextToClose.append(s[i])
		elif s[i] in right_b:
			# List already empty
			if (len(nextToClose) == 0):
				return False
			# close does not match open
			elif (s[i] != my_dict[nextToClose[-1]]):
				return False
			else:   
				nextToClose.pop()	
		i = i + 1		
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
		
