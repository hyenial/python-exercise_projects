'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position 
in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

#http://radiusofcircle.blogspot.com

#time module for execution time
import time

#time at the start of execution
start = time.time()

#function to return the value of name score
def name_score(name):
	letters = list(name)
	letters = [ord(x)-64 for x in letters]
	return sum(letters)

#reading the contents in the file
with open('names.txt') as f:
	a = f.read()

a = a.strip().split(',')

a = [x[1:-1] for x in a]

#sorting the values of the list
a.sort()

#total score
scores = 0

#counting the total score
for i in xrange(len(a)):
	scores += name_score(a[i])*(i+1)

#printing the total score
print scores

#time at the end of execution
end = time.time()

#total time for execution
print end-start
