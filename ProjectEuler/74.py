'''

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; 
it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

'''
# Python version = 2.7.2
# Platform = win32
 
import math
import time
 
def factorials_dict():
    """Create a dictionary of factorials 0 - 9"""
    d = {}
    for i in xrange(0, 10):
        d[i] = math.factorial(i)
    return d
 
def main():
    """Main Program"""
    start_time = time.clock()
    longest_chain = 0
    number_of_chains = 0
    factorials = factorials_dict()
    for number in xrange(66, 1000001):
        counter = 1
        switch = 1
        chain_element = number
        chainList = [number]
        while switch == 1:
            chain_element = str(chain_element)
            sum_factorials = 0
            for integer in chain_element:
                sum_factorials = factorials[int(integer)] + sum_factorials
            chain_element = sum_factorials
            if chain_element not in chainList:
                chainList.append(chain_element)
                counter += 1
            else:
                switch = 0
        if counter > longest_chain:
            number_of_chains = 1
            longest_chain = counter
        elif counter == longest_chain:
            number_of_chains += 1
        else:
            continue
    print "longest_chain = ", longest_chain
    print "number_of_chains = ", number_of_chains
    run_time = time.clock() - start_time
    print "Run time = ", run_time
             
if __name__ == '__main__':
    main()
