'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

# solution wat 1
#http://radiusofcircle.blogspot.com

#importing factorial function from math
from math import factorial

#time module for execution time calculation
import time

#time at the start of execution
start = time.time()

#creating a list with the digits of factorial
a = list(str(factorial(100)))

#converting the string to int
a = [int(x) for x in a]

#sum of the numbers
#factorial digit sum(fds)
fds = sum(a)

#time at the end of execution
end = time.time()

#print execution time and the solution
print 'Found {} in {} seconds'.format(fds,end-start)
