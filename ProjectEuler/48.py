'''
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.


'''
# http://radiusofcircle.blogspot.com
import time

# time at the start of program execution
start = time.time()

# solution variable
sol = 0

# for loop to loop till 1000
for i in xrange(1, 1001):
    sol += i**i

# printing the last 10 digits
print str(sol)[-10:]

# time at the end of program execution
end = time.time()

# printing the total time for execution
print end - start
