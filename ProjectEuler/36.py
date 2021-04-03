'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

'''
#http://radiusofcircle.blogspot.com

#time module for calculating execution time
import time

#time at the start of program execution
start = time.time()

#solution to add the values for each iteration
solution = 0

#looping through odd numbers
for i in xrange(1,1000000,2):
	#checking the base 10 number
	if str(i) == str(i)[::-1]:
		#checking the base 2 number
		if bin(i)[2:] == bin(i)[2:][::-1]:
			solution += i

#printing the number of instances
print solution

#time at the end of program execution
end = time.time()

#printing the execution time
print end - start
