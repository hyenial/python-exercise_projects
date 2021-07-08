'''
https://projecteuler.net/problem=67

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),
a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, 
as there are 299 altogether! If you could check one trillion (10^12) routes every second it would take over twenty billion years to check them all. 
There is an efficient algorithm to solve it. ;o)

<html>
<p>By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.</p>
<p class="monospace center"><span class="red"><b>3</b></span><br /><span class="red"><b>7</b></span> 4<br />
2 <span class="red"><b>4</b></span> 6<br />
8 5 <span class="red"><b>9</b></span> 3</p>
<p>That is, 3 + 7 + 4 + 9 = 23.</p>
<p>Find the maximum total from top to bottom in <a href="project/resources/p067_triangle.txt">triangle.txt</a> (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.</p>
<p class="smaller"><b>NOTE:</b> This is a much more difficult version of <a href="problem=18">Problem 18</a>. It is not possible to try every route to solve this problem, as there are 2<sup>99</sup> altogether! If you could check one trillion (10<sup>12</sup>) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)</p>
</html>

'''

#http://radiusofcircle.blogspot.com

#importing time module 
import time

#time at the start of execution
start = time.time()

with open('p67triangle.txt') as f:
	# All the numbers in the file
	number = f.read()

#splitting the number into a list
number = number.strip().split('\n')

#converting each and every list of strings to int
for i in xrange(1,len(number)):
	number[i] = number[i].strip().split(' ')
	number[i] = [int(x) for x in number[i]]

#adding the first number bcz we could not do the above
#operation as this one one number
number[0] = [59]

#counter for counting number of iterations
counter = 0

#for loop for bottom-up approach
for i in xrange(len(number)-2,-1,-1):
	for j in xrange(len(number[i])):
		number[i][j] = number[i][j] + max(number[i+1][j], number[i+1][j+1])
		counter += 1
	number.pop()

#printing the output
print 'Found {} in {} iterations'.format(number[0][0],counter)

#time at the end of execution
end = time.time()

#printing the total time
print end-start
