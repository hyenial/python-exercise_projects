'''
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n 
which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	1	2
3	1,2	2	1.5
4	1,3	2	2
5	1,2,3,4	4	1.25
6	1,5	2	3
7	1,2,3,4,5,6	6	1.1666...
8	1,3,5,7	4	2
9	1,2,4,5,7,8	6	1.5
10	1,3,7,9	4	2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

'''

# http://radiusofcircle.blogspot.com

# import time
import time

# start time
start = time.time()

# use xrange function if available
try:
    zrange = xrange
except:
    zrange = range

# function to calculate the value of
# n/phi(n)
def totient_function(prime_factors):
    multiplication = 1
    for factor in set(prime_factors):
        multiplication *= (1.0 - 1.0/factor)
    return 1.0/multiplication

# function to generate prime factors of numbers
# upto given number n
def prime_factors_generator(n):
    prime_factors = [[i] for i in zrange(n+1)]
    composite = [False]*(n+1)

    for i in zrange(3, int(n**0.5)+1, 2):
        if not composite[i]:
            for j in zrange(i, n/i+1, 2):
                mul = i*j
                prime_factors[mul] = [i] + prime_factors[j]
                composite[mul] = True

    for j in zrange(2, n/2+1):
        mul = 2*j
        prime_factors[mul] = [2] + prime_factors[j]
        composite[mul] = True
    return prime_factors


# generate prime factors upto 1000000
p_f = prime_factors_generator(1000000)

# remove 0, 1 from the list and find the
# value of n/phi(n)
p_f_nums = map(totient_function, p_f[2:])


# find the index of the maximum of p_h_nums
# add 2 to compensate the removal of 0, 1
print p_f_nums.index(max(p_f_nums))+2

# time at the end of the program
end = time.time()

# total time taken to execute the program
print end - start
{"mode":"full","isActive":false}
