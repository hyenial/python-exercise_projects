"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number,
that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

"""
import time
 
def factor(number):
    """Factor a number"""
    L = []
    for i in range(1, ((number / 2) + 1)):
        if number % i == 0:
            L.append(i)
    return L
 
def sum_factors(x):
    """Sum factors"""
    return sum(x)
 
def find_abundant_Set():
    """Find abundant Set"""
    abundant_Set = set()
    for m in range(0, 28123):
        x = factor(m)
        y = sum_factors(x)
        if m < y:
            abundant_Set.add(m)
        else:
            pass
    return set(sorted(abundant_Set))
 
def find_abundant_sums(xy):
    """Find abundant sums"""
    abundant_Set_a = set()
    for x in xy:
        for y in xy:
            zzz = x + y
            if zzz < 28123:
                abundant_Set_a.add(zzz)
            else:
                pass
    return set(sorted(abundant_Set_a))
 
def set_of_all_integers():
    """Set if all integers"""
    all_integers = set()
    for x in range(0, 28123):
        all_integers.add(x)
    return set(sorted(all_integers))
         
def find_missing_abundant_sums(yz, zz):
    """Find missing abundant sums"""
    all_positive_int = set()
    all_positive_int = zz - yz
    return set(all_positive_int)
 
def main():
    """Main program"""
    start_time = time.clock()
    xy = find_abundant_Set()
    yz = find_abundant_sums(xy)
    zz = set_of_all_integers()
    xz = find_missing_abundant_sums(yz, zz)
    tally = sum(xz)
    print "Tally = ", tally
    run_time = time.clock() - start_time
    print "Run time = ", run_time
             
if __name__ == '__main__':
    main()
