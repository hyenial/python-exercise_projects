'''
https://projecteuler.net/problem=64

'''


# http://radiusofcircle.blogspot.com
def continued_fraction(n):
    """
    This function will calculate
    Continued fraction of a given number"""
    integer = int(n)
    decimal = n - integer
    cf_list = [integer]
    if decimal != 0:
        while integer != 2*cf_list[0]:
            decimal_inv = 1/decimal
            integer = int(decimal_inv)
            decimal = decimal_inv - integer
            cf_list.append(integer)
    return cf_list
