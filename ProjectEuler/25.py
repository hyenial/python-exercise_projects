"""
1000-digit Fibonacci number

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

"""

#http://radiusofcircle.blogspot.com

#time module for execution time
import time

#time at the start of program
start = time.time()

#list to store the fibonacci numbers
# added first two numbers of the 
#fibonacci sequence
fib = [0,1]

#iterator
i = 2

#An infinite loop, breaks 
#when the number is 1000 digits long
while True:
	#using the function given in question
	fib_new = fib[i-1]+fib[i-2]
	#Appending the new fibonacci to the list
	fib.append(fib_new)
	#condition to check for 1000 digits
	if fib_new>10**999:
		print i
		break
	i = i+1

#time at the end of execution
end = time.time()

#printing the total time for execution
print end-start
