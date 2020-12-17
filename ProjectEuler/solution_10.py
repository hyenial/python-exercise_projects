"""
question 10: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
https://projecteuler.net/problem=10

"""

import math


def check_prime(num):
    if num > 2 and num % 2 == 0:
        return False
    else:
        # I tried using a generator here,
        # but it is slower by a noticeable amount.
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
    return True


def find_sum(limit):
    sum = 0
    for i in range(2, limit):
        if check_prime(i):
            sum += i
    
    return sum


if __name__ == '__main__':

    # Find the sum of all primes below two million
    print(find_sum(2000000))

    # confirm above is correct by solving example
    # and verifying results are euqal to that presented
    # by example
    print(find_sum(10))


# referance : https://gist.github.com/yelluw/f24b0c4020b479b37eeb7ff7e44eca7e
# https://repl.it/@harunyen/q10
