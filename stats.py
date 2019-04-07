""" Xin's own Python Library code, Statistics"""
'''
Copyright @Xin Wang
'''

'''
Demonstrate different ways of calculate variance and deviation
'''
import statistics
def standard_python_stats(l):
    print('\n' + ">>> Results with Standard Python Library:")
    print("Mean = " + str(statistics.mean(l)))
    print("pvariance = " + str(statistics.pvariance(l)))
    print("pstdev = " + str(statistics.pstdev(l)))
    '''
    Why variance and stdev (called sample *** uses /(n-1))?
    Bessel's correction
    '''
    print("variance = " + str(statistics.variance(l)))
    print("stdev = " + str(statistics.stdev(l)))

import numpy as np
def numpy_stats(l):
    np_arr = np.array(l)
    print('\n' + ">>> Results with numpy Library:")
    print("Mean = " + str(np.mean(np_arr)))
    '''
    By default, numpy gives population variance
    and deviation.
    '''
    print("pvariance = " + str(np.var(np_arr)))
    print("pstdev = " + str(np.std(np_arr)))
    '''
    Unless as we asked to give sample variance
    and sample standard deviation.
    ddof: Delta Degrees of Freedom
    '''
    print("variance = " + str(np.var(np_arr, ddof=1)))
    print("stdev = " + str(np.std(np_arr, ddof=1)))


'''
Now, some interesting stuff, the famous welford's method:
Stream of data!!!
'''
import math
class welford :
    # num of elements seen so far.
    count = 0
    # mean so far
    m = 0.0
    # last(previous) mean
    m_last = 0.0
    # current sumary of variance
    s = 0.0
    # last(previous) summary of variance
    s_last = 0.0
 
    def ingest(self, x):
        if(self.count == 0):
            self.m_last = x
            self.s_last = 0.0
        else:
            self.m_last = self.m
            self.s_last = self.s
        self.count += 1
        self.m = self.m_last + (x - self.m_last)/self.count
        '''
        This is the magic !!! See
        https://alessior.wordpress.com/2017/10/09/onlinerecursive-variance-calculation-welfords-method/
        '''
        self.s = self.s_last + (x - self.m_last) * (x - self.m)
 
    def mean(self):
        return self.m
 
    def var(self):
        if (self.count < 2):
            return 0
        else:
            return self.s/(self.count - 1)
 
    def stdev(self):
        return math.sqrt(self.var())
    
    def pvar(self):
        if (self.count < 1):
            return 0
        else:
            return self.s/(self.count)
 
    def pstdev(self):
        return math.sqrt(self.pvar())
 
def welford_stats(l):
    print('\n' + ">>> Results with Welford method:")
    my_class = welford()
    for value in l:
        my_class.ingest(value)
    print("Mean = " + str(my_class.mean()))
    print("pvariance = " + str(my_class.pvar()))
    print("pstdev = " + str(my_class.pstdev()))
    print("variance = " + str(my_class.var()))
    print("stdev = " + str(my_class.stdev()))   

if __name__ == '__main__':
    sl = [1, 2, 3, 4, 5, 5]
    print(sl)
    standard_python_stats(sl)
    numpy_stats(sl)
    welford_stats(sl)
    

