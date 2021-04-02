'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
'''
#http://radiusofcircle.blogspot.com

#time module for calculation of execution time
import time

#time at the start of program execution
start = time.time()

#Sieve of Erotosthenes
#One of the best algorithm to generate prime numbers
#https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sieve(n):
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
	is_prime[2] = True
	#even numbers except 2 have been eliminated
	for i in xrange(3,int(n**0.5+1),2):
		index = i*2
		while index < n:
			is_prime[index] = False
			index = index+i
	prime = [2]
	for i in xrange(3,n,2):
		if is_prime[i]:
			prime.append(i)
	return (prime)

#sieving prime numbers upto 1 million
primes = sieve(1000000)

#counter to count the instances
counter = 0

#looping through prime numbers
for i in primes:
	#assuming that there is no 2,4,6,8,5,0 in digits
	flag = True
	#start with tens digit
	number = i/10
	#looping through digits
	while number:
		if (number%10) % 2 == 0 or (number%10)%5 == 0:
			flag = False
			break
		number //= 10
	#check if flag is true or false
	if flag:
		length = len(str(i))
		number = i
		#assume that the circular permutations are prime
		counter += 1
		#loop to create circular permutations
		for j in xrange(length):
			number = (number%10)*10**(length-1)+number//10
			#if any permutation is not prime
			if number not in primes:
				#subtract one from counter
				counter -= 1
				break

#print the number of instances
print counter

#time at the end of program execution
end = time.time()

#printing the total time for execution
print (end - start)

