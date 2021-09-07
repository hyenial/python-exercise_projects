'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

'''

# http://radiusofcircle.blogspot.com

# time module
import time

# sqrt method
from math import sqrt
# time at the start of program execution
start = time.time()


def is_prime(n):
    """function to check if the given
    number is prime or not"""
    if n % 2 == 0:
        return False
    else:
        for i in xrange(3, int(n**0.5+1),2):
            if n % i == 0:
                return False
        return True

# iterator
number = 3

# list of primes
primes = [2]


# while loop
while True:
    if is_prime(number):
        primes.append(number)
    else:
        for i in primes:
            if math.sqrt(((number-i)/2)) == int(math.sqrt(((number-i)/2))):
                break
        else:
            print number
            break

    number += 2

# time at the end of program execution
end = time.time()

# total time of execution
print end - start
