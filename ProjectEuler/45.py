'''
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.

'''

# http://radiusofcircle.blogspot.com

# time module
import time

# time at the star of program execution
start = time.time()


def is_pentagonal(p):
    """function to check if the
    given number is pentagonal"""
    if (1+(24*p+1)**0.5) % 6 == 0:
        return True
    return False


def is_hexagonal(h):
    """function to check if the
    given number is hexagonal"""
    if (1+(8*h+1)**0.5) % 4 == 0:
        return True
    return False

# iterator start after 285
i = 286

# while loop for iterating
while True:
    triangle = i*(i+1)/2
    if is_pentagonal(triangle) and is_hexagonal(triangle):
        print triangle
        break
    i += 1

# time at the end of program execution
end = time.time()
