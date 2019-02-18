""" Xin's own Python math library """
'''
Copyright @Xin Wang
'''
def isPrime(n):
    """Check if an int is a Prime number."""
    n = int(n)
    if (n <= 1):
        return False
    elif (n == 2):
        return True
    else: #n >= 3
        for b in range(2, (int(n/2) + 1)):
            if (n % b == 0):
                return False
    return True

