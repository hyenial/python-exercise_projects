'''
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

'''

# http://radiusofcircle.blogspot.com

# import time module
import time

# time at the start of program execution
start =  time.time()

# counter to count the number of instances
counter = 0

# for loop to loop from 1 to 9
for i in xrange(1, 10):
    power = 1
    while True:
        if power == len(str(i ** power)):
            counter += 1
        else:
            break
        power += 1

# print the number of instances found
print counter

# time at the end of program execution
end = time.time()

# total time taken for the program execution
print end - start
