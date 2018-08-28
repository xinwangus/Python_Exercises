#!/usr/bin/env python

# A test program to check if a string containing
# [] {} () are properly closed, and no interlace

# Very similiar to the C++ version I wrote, but use
# python list to simulate a "stack"


def isClosed (s):
        i = 0
	l = len(s)

        nextToClose = [] # it is a list of two-member-list
        # 1st member is the count of next to close
        # 2nd member is the what is the next to close
	# example: "{{[[[(" would give:
        # [ [2, '}'] [3, ']'] [1, ')'] ]
    
	while i < l:
		if s[i] == '{':
			if len(nextToClose) == 0 or nextToClose[-1][1] != '}':
				nextToClose.append([1, '}'])
			else:
				nextToClose[-1][0] += 1
		elif s[i] == '[':
                        if len(nextToClose) == 0 or nextToClose[-1][1] != ']':
                                nextToClose.append([1, ']'])
                        else:   
                                nextToClose[-1][0] += 1
		elif s[i] == '(':
                        if len(nextToClose) == 0 or nextToClose[-1][1] != ')':
                                nextToClose.append([1, ')'])
                        else:   
                                nextToClose[-1][0] += 1
		elif s[i] == '}':
			if len(nextToClose) == 0 or nextToClose[-1][1] != '}':
				return False
                        else:
				nextToClose[-1][0] -= 1
				if nextToClose[-1][0] == 0:
					nextToClose.pop()
		elif s[i] == ']':
			if len(nextToClose) == 0 or nextToClose[-1][1] != ']':
				return False
                        else:
				nextToClose[-1][0] -= 1
				if nextToClose[-1][0] == 0:
					nextToClose.pop()
		elif s[i] == ')':
			if len(nextToClose) == 0 or nextToClose[-1][1] != ')':
				return False
                        else:
				nextToClose[-1][0] -= 1
				if nextToClose[-1][0] == 0:
					nextToClose.pop()
		#print(nextToClose)
		i = i + 1	

	if len(nextToClose) != 0:
		return False
	else:
		return True


while True:
	print("String to check:")

	# can just use  input() with python 3
	ss = raw_input()

	if isClosed(ss):
		print (ss + " is Properly Closed, Good Job!")
	else:
		print (ss + " is not Properly Closed!")
		
