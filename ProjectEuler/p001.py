# !/usr/bin/env python
# Referance: https://wiki.python.org/moin/ProblemSets/Project%20Euler%20Solutions

# Problem 1: Add all the natural numbers below 1000 that are multiples of 3 or 5.
# http://projecteuler.net/index.php?section=problems&id=1

    def multiples_of_3_or_5():
        for number in xrange(1000):
            if not number % 3 or not number % 5:
                yield number

    print sum(multiples_of_3_or_5())
    
# In one line:
    print sum( number for number in xrange(1000) if not (number % 3 and number % 5) )

    

