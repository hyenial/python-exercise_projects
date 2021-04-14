'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

'''

# http://radiusofcircle.blogspot.com

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

# variable to store the values
a = ''

# for loop
for i in xrange(1, 185186):
    a += str(i)

# d1
d1 = int(a[0])

# d10
d10 = int(a[9])

# d100
d100 = int(a[99])

# d1000
d1000 = int(a[999])

# d10000
d10000 = int(a[9999])

# d100000
d100000 = int(a[99999])

# d1000000
d1000000 = int(a[999999])

# printing the solution
print d1*d10*d100*d1000*d10000*d100000*d1000000

# time at the end of program execution
end = time.time()

# total time for execution
print end - start
view raw
