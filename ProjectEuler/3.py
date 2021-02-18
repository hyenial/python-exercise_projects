# question 3:  Find the largest prime factor of 317584931803.

    plist = [2]

    def primes(min, max):
        if 2 >= min: yield 2
        for i in range(3, max, 2):
            for p in plist:
                if i%p == 0 or p*p > i: break
            if i%p:
                plist.append(i)
                if i >= min: yield i
        
    def factors(number):
        for prime in primes(2, number):
            if number % prime == 0:
                number /= prime
                yield prime
            if number == 1:
                break

    print max(factors(317584931803))
