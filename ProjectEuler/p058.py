'''

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, 
but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above,
a square spiral with side length 9 will be formed. If this process is continued, 
what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

'''

# http://radiusofcircle.blogspot.com

# time module for calculating the execution time
import time

# time at the start of program execution
start = time.time()


def is_prime(n):
    """function to find if the given
    number is prime"""
    for i in xrange(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

# iterator for the numbers
i = 0

# gap for every four iterations
gap = 1

# ratio of lenght of primes to length of diagonals
ratio = 1

# prime numbers on the diagonal
primes = []

# all the numbers, including 1
all_numbers = [1]

# While loop, to loop until we reach the last number
while ratio > 0.1:
    for j in xrange(4):
        # generating the value of n for 2n+1
        i += gap
        # generating the odd number
        present_number = 2*i + 1
        # appending the number to all_numbers
        all_numbers.append(present_number)
        # appending to prime if the number is prime
        if is_prime(present_number):
            primes.append(2*i + 1)
    # changing the value of ratio at the end of loop
    ratio = float(len(primes))/len(all_numbers)
    # increasing the gap after every 4 numbers
    gap += 1

# printing the side length
print (2*i+1)**0.5

# time at the end of the program execution
end = time.time()

# printing the total time of execution
print end - start
