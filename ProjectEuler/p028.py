"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?



"""

#http://radiusofcircle.blogspot.com

#time module for calculating the execution time
import time

#time at the start of program execution
start = time.time()

#last number of the maximum number
last_number = 1001*1001

#generating odd numbers list
odd_numbers = xrange(1,last_number+1,2)

#iterator the numbers
i = 0

#gap for every four iterations
gap = 1

#answer
solution = 1

#While loop to loop until we reach the last number
while odd_numbers[i] != last_number:
	for j in xrange(4):
		i+= gap
		solution += odd_numbers[i]
	gap += 1

#printing the solution
print solution

#time at the end of the program execution
end = time.time()

#printing the total time of execution
print end - start
