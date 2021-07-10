'''
https://projecteuler.net/problem=68


<p>Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.</p>
<div class="center">
<img src="project/images/p068_1.png" class="dark_img" alt="" /><br /></div>
<p>Working <b>clockwise</b>, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), 
each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.</p>
<p>It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.</p>
<div class="center">
<table width="400" cellspacing="0" cellpadding="0"><tr><td width="100"><b>Total</b></td><td width="300"><b>Solution Set</b></td>
</tr><tr><td>9</td><td>4,2,3; 5,3,1; 6,1,2</td>
</tr><tr><td>9</td><td>4,3,2; 6,2,1; 5,1,3</td>
</tr><tr><td>10</td><td>2,3,5; 4,5,1; 6,1,3</td>
</tr><tr><td>10</td><td>2,5,3; 6,3,1; 4,1,5</td>
</tr><tr><td>11</td><td>1,4,6; 3,6,2; 5,2,4</td>
</tr><tr><td>11</td><td>1,6,4; 5,4,2; 3,2,6</td>
</tr><tr><td>12</td><td>1,5,6; 2,6,4; 3,4,5</td>
</tr><tr><td>12</td><td>1,6,5; 3,5,4; 2,4,6</td>
</tr></table></div>
<p>By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.</p>
<p>Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum <b>16-digit</b> string for a "magic" 5-gon ring?</p>
<div class="center">
<img src="project/images/p068_2.png" class="dark_img" alt="" /><br /></div>



'''

# http://radiusofcircle.blogspot.com

# time module
import time

# time at the start of program execution
start = time.time()

# numbers from 1-10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def convert_to_num(a, b, c, d, e, f, g, h, i, j):
	"""
	Function to convert a-j to
	required string based on the criteria
	"""
	big_num = {a:0, d:1, f:2, h:3, j:4}
	break_num = big_num[min(big_num.keys())]
	nums = [(a,b,c), (d,c,e), (f,e,g), (h,g,i), (j,i,b)]
	nums = nums[break_num:]+nums[:break_num]
	string = ''
	for num_tup in nums:
		for num in num_tup:
			string += str(num)
	return string

# list to store solutions
avail_sol  = []

# start with all the numbers
for a in numbers:
	numbers_b = numbers[:]
	numbers_b.remove(a)
	# numbers without a
	for b in numbers_b:
		numbers_c = numbers_b[:]
		numbers_c.remove(b)
		# numbers without a, b
		for c in numbers_c:
			line_sum = a+b+c
			numbers_d = numbers_c[:]
			numbers_d.remove(c)
			# numbers without a, b, c
			for d in numbers_d:
				numbers_e = numbers_d[:]
				numbers_e.remove(d)
				e = line_sum - c - d
				# numbers without a, b, c, d
				if e in numbers_e:
					numbers_f = numbers_e[:]
					numbers_f.remove(e)
					# numbers without a, b, c, d, e
					for f in numbers_f:
						numbers_g = numbers_f[:]
						numbers_g.remove(f)
						g = line_sum - e - f
						# numbers without a, b, c, d, e, f
						if g in numbers_g:
							numbers_h = numbers_g[:]
							numbers_h.remove(g)
							# numbers without a, b, c, d, e, f, g
							for h in numbers_h:
								numbers_i = numbers_h[:]
								numbers_i.remove(h)
								i = line_sum - g - h
								# check if i is in numbers_i list
								if i in numbers_i:
									j = line_sum - i - b
									numbers_j = numbers_i[:]
									numbers_j.remove(i)
									# numbers without a, b, c, d, e, f, g, h, i
									if j in numbers_j:
										ctn = convert_to_num(a, b, c, d, e, f, g, h, i, j)
										avail_sol.append(ctn)

# solution will be the maximum of all the numbers
sol = max([int(x) if len(x) == 16 else 0 for x in avail_sol])

# print the solution
print sol

# time at the end
end = time.time()

# total time taken
print end - start
