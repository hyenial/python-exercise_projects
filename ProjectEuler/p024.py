"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""

#http://radiusofcircle.blogspot.com

#time for calculation of execution time
import time

#import permutations from itertools
from itertools import permutations

#time at the start of program execution
start = time.time()

#Generating Lexicographic permutations with python
#converting the solution to a list
#as it is returned as itertools.permutations object
lexi_perm = list(permutations('0123456789'))

#Each permutation is in the form of tuple
#so join all the strings to get solution
solution = ''.join(lexi_perm[999999])

#printing the solution
print solution

#time at the end of execution
end = time.time()

#printing the total time taken
print end - start

