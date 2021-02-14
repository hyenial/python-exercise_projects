
'''
question 16.
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''

import math

def sumOfDigit(num):
    sum_of_digits = 0
    while num > 9:
        sum_of_digits += num % 10
        num = int(num/10)
    sum_of_digits += num
    return sum_of_digits

print sumOfDigit(math.pow(2,1000))
