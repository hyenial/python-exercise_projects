'''
A googol (10**100) is a massive number: one followed by one-hundred zeros; 
100100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?

'''
# http://radiusofcircle.blogspot.com

# time module
import time

# time at the start of program execution
start = time.time()


def sum_of_digits(n):
    """sum of digits of given number"""
    sod = 0
    while n != 0:
        sod += n % 10
        n //= 10
    return sod

# largest sum of digits
largest = 0

# for loop to get a and b
for a in xrange(0, 100):
    for b in xrange(0, 100):
        sod = sum_of_digits(a**b)
        if sod > largest:
            largest = sod

# printing the largest sum of digits
print largest

# time at the end of program execution
end = time.time()

# total time for execution
print end - start
