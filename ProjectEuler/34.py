'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

'''

#http://radiusofcircle.blogspot.com

#factorial function for calculating factorial
from math import factorial

#time module for calculating time of execution
import time

#time at the start of program execution
start = time.time()

#factorials of numbers from 0-9
f = [factorial(0),
factorial(1),
factorial(2),
factorial(3),
factorial(4),
factorial(5),
factorial(6),
factorial(7),
factorial(8),
factorial(9)]

#sum of factorial of the digits
def factorial_digits(n):
	s = 0
	while n:
		s += f[n%10]
		n //= 10
	return s

#variable to save the value of solution
solution = 0

#for loop to loop till 1854721
for i in xrange(10,1854721):
	if factorial_digits(i) == i:
		solution += i

#printing the solution
print (solution)

#Time at the end of program execution
end = time.time()

#total time of execution
print (end - start)
