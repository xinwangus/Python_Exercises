#!/usr/bin/env python

def isPrime(n):
	if (n <= 1):
		return False
	elif (n == 2):
		return True
	else: #n >= 3
		for b in range(2, (n-1)):
			if (n % b == 0):
				return False
		return True

def checkPrime(n):
	if isPrime(n):
		print(str(n) + " is a Prime Number :-)")
	else:
		print(str(n) + " is -not- a Prime Number!")
		

if __name__ == '__main__':
	for i in range(0, 100):
		checkPrime(i)
	while True:
		n = int(input("\n\nNumber to check?: "))
		checkPrime(n)
