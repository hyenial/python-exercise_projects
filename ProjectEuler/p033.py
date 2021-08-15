'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, 
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, 
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.


'''

#http://radiusofcircle.blogspot.com

#time module for calculation of execution time
import time

#importing fractions module
from fractions import Fraction

#time at the start of program execution
start = time.time()

#Product of all the four fractions say 1 for now
product = 1

#'for' loops to generate Numerator and Denominator
for i in xrange(10,100):
	for j in xrange(i+1,100):
		#Intersection of Two sets(Common number between the two)
		common = list(set(str(i))&set(str(j)))
		#Check if the list is not empty
		if len(common) != 0:
			#Check if the common number is not 0
			if common[0] != '0':
				num = list(str(i))
				den = list(str(j))
				#Remove the common element from numerator
				num.remove(common[0])
				#Remove the common element from Denominator
				den.remove(common[0])
				#Check if the value of num and den are not equal to 0
				if num[0]!='0' and den[0]!='0':
					#Check if they satisfy the question condition
					if Fraction(int(num[0]),int(den[0])) == Fraction(i,j):
						#multiply to the product
						product *= Fraction(i,j)

#print the denominator of the resulting fraction
print product.denominator

#time at the end of program execution
end = time.time()

#Printing the total time for execution
print end - start
