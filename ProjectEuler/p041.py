'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?


'''
#!/usr/bin/python

# http://radiusofcircle.blogspot.com

# importing the permutations method
from itertools import permutations

# importing time module
import time

# time at the start of program execution
start = time.time()


def is_prime(n):
    """Function to check if
    the given number is prime"""
    for i in xrange(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# permutations of numbers from 1-7
p = permutations('1234567')

# for loop to loop from reverse order
# from higher to lower
for i in list(p)[::-1]:
    if int(i[6]) % 2 != 0:
        number = int(''.join(i))
        if (number+1) % 6 == 0 or (number-1) % 6 == 0:
            if is_prime(number):
                print number
                break

# time at the end of program execution
end = time.time()

# total time of execution
print end-start
