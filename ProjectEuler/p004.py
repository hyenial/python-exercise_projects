# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Question 4.Find the largest palindrome made from the product of two 3-digit numbers.

def compute():
	ans = max(i * j
		for i in range(100, 1000)
		for j in range(100, 1000)
		if str(i * j) == str(i * j)[ : : -1])
	return str(ans)


if __name__ == "__main__":
	print(compute())
  
 # referance : # https://www.nayuki.io/page/project-euler-solutions
