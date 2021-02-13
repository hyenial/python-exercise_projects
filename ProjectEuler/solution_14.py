'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

#http://radiusofcircle.blogspot.com

#time module for execution time
import time

#Time at the start of execution
start = time.time()

#collatz function straight forward
def collatz(n):
 """
 This function will take
 a number and it will return
 the size of the collatz
 sequence for input n"""
 counter = 1
 while n>1:
  if n%2 == 0:
   n = n/2
   counter += 1
  else:
   n = 3*n+1
   counter += 1
  if n == 1:
   return counter

#let the largest number be 0
largest_number = 0

#let the largest sequence size be 0
large_seq = 0

#for loop for 1 million
for i in xrange(1000000,1,-1):
 #size of collatz for the iteration
 n = collatz(i)
 #if size if greater than previous
 #replace it with the new one
 if n > large_seq:
  largest_number = i
  large_seq = n

#printing the largest number
print largest_number

#time at the end of execution
end = time.time()

#Printing the total time taken
print end-start
