"""
urprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

"""

#http://radiusofcircle.blogspot.com

#time module for calculating execution time
import time

#time at the start of program execution
start = time.time()

#Let the sum be 0 at the start
solution = 0

#for loop to loop till 5(10-1)^5
for i in xrange(2,5*9**5+1):
	if sum([int(x)**5 for x in str(i)]) == i:
		solution += i

#printing the solution
print solution

#time at the end of execution
end = time.time()

#printing the total execution time
print end - start
