'''
question9: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''

for a in range(3, 1000):
    for b in range (a + 1, 999):
        cSquared = a**2 + b**2
        c = cSquared**0.5

        if a + b + c == 1000:
            product = a * b * c
            print(product)
            break
            
            
  # referance: https://code.mikeyaworski.com/python/project_euler/problem_9
