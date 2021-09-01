'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, 
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.

'''
# http://radiusofcircle.blogspot.com

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()


def converter(z):
    """function to make a given
    number to a three digit number
    by adding zeros at front"""
    if len(z) == 2:
        return '0'+z
    elif len(z) == 1:
        return '00'+z
    return z


def m(n):
    """function to generate multiples
    of given number under 1000"""
    mn = []
    mul = 1
    i = 1
    while mul < 1000:
        mul = i*n
        i += 1
        mn.append(mul)
    mn.pop()
    mn = map(str, mn)
    mn = map(converter, mn)
    return mn


def concat(a, b):
    """function to form the solution"""
    c = []
    for i in a:
        for j in b:
            if i[:2] == j[1:] and len(set(j[0] + i)) == len(j[0] + i):
                c.append(j[0] + i)
    return c


def missing(g):
    """function to add the missing number from
    0-9 to complete the pandigital number"""
    for i in '0123456789':
        if i not in g:
            return i + g

# forming the multiples of 2,3,5,7,11,13
m17, m13, m11, m7, m5, m3, m2 = (m(17), m(13), m(11), m(7), m(5), m(3), m(2))

# getting the required solution
d = reduce(concat, [m17, m13, m11, m7, m5, m3, m2])

# adding the missing number
d = map(missing, d)

# converting the numbers to int
d = map(int, d)

# printing the sum of numbers
print sum(d)

# time at the end of execution
end = time.time()

# printing the total time for execution
print end - start
