'''
The number 3797 has an interesting property. Being prime itself, 
it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

'''


#http://radiusofcircle.blogspot.com

#time module for calculating the execution time
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
	return prime

#prime numbers less than 1 million
primes = sieve(1000000)

#solution set to store values
solution = []

#for loop, to loop through primes
for prime in primes:
	flag = True
	number = prime
	mul = 10**(len(str(number))-1)
	number = (number-(number/mul)*mul)/10
	#checks if number has any digits with 
	#multiples of 2 or 5
	while number:
		if (number%10) % 2 == 0 or (number%10) %5 == 0:
			flag = False
			break
		number = number/10
	#check for right truncatability	
	if flag:
		number = prime/10
		solution.append(prime)
		while number:
			if number not in primes:
				solution.remove(prime)
				break
			number //= 10

#copy of solution set, removed - 2,3,5,7
sol = solution[4:]

#for loop to check for left truncatability
for i in sol:
	number = i
	while number:
		mul = 10**(len(str(number))-1)
		number = number - (number/mul)*mul
		if number not in primes and number != 0:
			solution.remove(i)
			break

#printing the sum of solution
print sum(solution)

#time at the end of program execution
end = time.time()

#printing the execution time
print end - start
