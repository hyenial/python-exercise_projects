'''

Consider quadratic Diophantine equations of the form:

x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is ^square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 – 2×2^2 = 1
2^2 – 3×1^2 = 1
9^2 – 5×4^2 = 1
5^2 – 6×2^2 = 1
8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.


'''

# http://radiusofcircle.blogspot.com

#import time
import time

# square root function
from math import sqrt

# time at the start of program execution
start = time.time()

# function to calculate the continued fraction
def cf(n):
    mn = 0.0
    dn = 1.0
    a0 = int(sqrt(n))
    an = int(sqrt(n))
    convergents = [a0]
    period = 0
    if a0 != sqrt(n):
        while an != 2*a0:
            mn = dn*an - mn
            dn = (n - mn**2)/dn
            an = int((a0 + mn)/dn)
            convergents.append(an)
    return convergents[:-1]

def cf_inv(cf):
    """
    function to calculate the
    simple fraction from the continued
    fraction.
    """
    numerator = 1
    denominator = cf.pop()
    while cf:
        denominator, numerator = denominator*cf.pop() + numerator, denominator
    return denominator, numerator

# variable to store the largest value 
# and the place it occurs
largest = 0, 0

# for loop less than 1000
for i in xrange(1, 1001):
    if i%sqrt(i) != 0:
        continued_fraction = cf(i)
        if len(continued_fraction) % 2 != 0:
            u, v = cf_inv(continued_fraction)
            u, v = 2*u**2+1, 2*u*v
        else:
            u, v = cf_inv(continued_fraction)
        if u > largest[1]:
            largest = i, u

# print the largest value
print largest[0]

# time at the end of program execution
end = time.time()

# total time taken to run the program
print end - start
