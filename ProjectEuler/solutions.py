# Problem 1: Add all the natural numbers below 1000 that are multiples of 3 or 5.
# http://projecteuler.net/index.php?section=problems&id=1
    def multiples_of_3_or_5():
        for number in xrange(1000):
            if not number % 3 or not number % 5:
                yield number

    print sum(multiples_of_3_or_5())
    
# In one line:
    print sum( number for number in xrange(1000) if not (number % 3 and number % 5) )

    
# Problem 2: Find the sum of all the even-valued terms in the Fibonacci sequence which do not exceed one million.

    def fib():
        x,y = 0,1
        while True:
            yield x
            x,y = y, x+y

    def even(seq):
        for number in seq:
            if not number % 2:
                yield number

    def under_a_million(seq):
        for number in seq:
            if number > 1000000:
                break
            yield number   

    print sum(even(under_a_million(fib())))
    
    #Alternately
        import itertools

    def fib():
        x,y = 0,1
        while True:
            yield x
            x,y = y, x+y

    print sum(x for x in itertools.takewhile(lambda x: x <= 1000000, fib()) if x % 2 == 0)
