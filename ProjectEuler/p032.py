'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 
15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

#http://radiusofcircle.blogspot.com

#time module for calculating the execution time
import time

#time at the start of execution
start = time.time()

#We will store the products in a set to avoid duplicates
products = set()

#Digits from 1-9 which will be checking later
to_be_checked = set('123456789')

#for single digit multiplicand
for i in xrange(9):
	for j in xrange(999,9999):
		s = str(i)+str(j)+str(i*j)
		if len(s) == 9 and set(s) == to_be_checked:
			products.add(i*j)
		elif len(s) > 9:break

#for double digit multiplicand
for i in xrange(9,99):
	for j in xrange(99,999):
		s = str(i)+str(j)+str(i*j)
		if len(s) == 9 and set(s) == to_be_checked:
			products.add(i*j)
		elif len(s)>9: break

#printing the result
print sum(products)

#time at the end of execution
end = time.time()

#total time taken for execution
print end - start
