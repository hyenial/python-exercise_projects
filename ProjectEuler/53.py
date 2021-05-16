'''
https://projecteuler.net/problem=53

'''

# http://radiusofcircle.blogspot.com

# time module
import time

# import factorial function as f
from math import factorial as f

# time at the start of program execution
start = time.time()

# counter to count the number of instances
counter = 0


def ncr(n, r):
    """a function to find the
    combinatorics"""
    return f(n)/(f(r)*f(n-r))

# for loops
for n in xrange(23, 101):
    for r in xrange(4, n-3):
        if ncr(n, r) > 1000000:
            counter += 1

# printing the number of instances
print counter

# time at the end of program execution
end = time.time()

# total time for execution
print end - start
