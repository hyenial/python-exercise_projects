
'''

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). 
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

'''
# http://radiusofcircle.blogspot.com

# import time
import time

# time at the start of program
start = time.time()

# list to store cubes
cubes = []

# iterator
i = 0

# while loop
while True:
 # cube of the number
 cube = sorted(list(str(i**3)))
 # appending the cube to cubes list
 cubes.append(cube)
 # check if it occured 5 times
 if cubes.count(cube) == 5:
  # print the cube of the smallest such cube
  print (cubes.index(cube))**3
  break
 i += 1

# time at the end of program
end = time.time()

# total time taken
print end - start
