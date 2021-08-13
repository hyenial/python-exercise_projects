'''
n the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

'''

#http://radiusofcircle.blogspot.com

#time module for calculating execution time
import time

#time at the start of the program execution
start = time.time()

#counter for couting number of possibilities
counter = 0

# number of 100p coins
for a in xrange(3):
	# number of 50p coins
		for b in xrange(1+(200-100*a)/50):
			# number of 20p coins
				for c in xrange(1+(200-100*a-50*b)/20):
					# number of 10p coins
						for d in xrange(1+(200-100*a-50*b-20*c)/10):
							# number of 5p coins
								for e in xrange(1+(200-100*a-50*b-20*c-10*d)/5):
									# number of 2p coins
										for f in xrange(1+(200-100*a-50*b-20*c-10*d-5*e)/2):
											counter += 1

# Total number of ways we can form the 200p
# Added 1 for 200p case
print counter+1

#time at the end of program execution
end = time.time()

#Total time taken for the program execution
print end - start
