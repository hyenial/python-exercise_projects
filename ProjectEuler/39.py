'''

If p is the perimeter of a right angle triangle with integral length sides, a,b,c, there are exactly three solutions for p=120.

{20,48,52},{24,45,51},{30,40,50}
For which value of p≤1000, is the number of solutions maximised?

'''


# http://radiusofcircle.blogspot.com

# time module for calculating execution time
import time

# Counter method
from collections import Counter

# time at the start of program execution
start = time.time()

# list to store perimeters
perimeters = []

# looping to generate a,b and c
for a in xrange(1, 500):
    for b in xrange(a, 500):
        c = (a**2 + b**2)**0.5
        if int(c) == c and a + b + c <= 1000:
            perimeters.append(a+b+c)

# counting the instances of perimeters
p = Counter(perimeters)

# printing the most common perimeter
# or printing the most repeated perimeter
print p.most_common(1)[0]

# time at the end of program execution
end = time.time()

# printing the total execution time
print end - start
