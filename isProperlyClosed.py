#!/usr/bin/env python3

# A test program to check if a string containing
# [] {} () are properly closed, and no interlace

# Very similiar to the C++ version I wrote, but use
# python list to simulate a "stack"
def isClosed (s):
	i = 0
	l = len(s)
	nextToClose = []
    
	while i < l:
		if s[i] == '{' or s[i] == '(' or s[i] == '[' :
			nextToClose.append(s[i])
		elif s[i] == ']':
			if (len(nextToClose) == 0) or (nextToClose[-1] != '['):
				return False
			else:   
				nextToClose.pop()
		elif s[i] == '}':
			if (len(nextToClose) == 0) or (nextToClose[-1] != '{'):
				return False
			else:   
				nextToClose.pop()
		elif s[i] == ')':
			if (len(nextToClose) == 0) or (nextToClose[-1] != '('):
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
		
