'''
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?

'''

#Project Euler Problem 73

def ceildiv(a, b): return -(-a // b)

def p(L, n1=1, d1=3,  n2=1, d2=2):
    n = [0] * (L+1) 
    for d in xrange(1, L+1):
        n[d] += ceildiv(n2*d, d2) - ceildiv(n1*d, d1) - 1
        n[2*d::d] = [k-n[d] for k in n[2*d::d]]
    return sum(n)

print p(12000), "fractions found in range."

