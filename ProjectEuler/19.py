'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''

#http://radiusofcircle.blogspot.com

#importing time and calendar moduler 
import time,calendar


#time at the start of execution
start = time.time()

#changing the preference from monday to sunday
calendar.setfirstweekday(6)


def sundays(year):
	"""This function returns 
	The number of sundays in a year
	on the first of the month"""
	counter = 0
	for month in xrange(1,13):
		cal = calendar.monthcalendar(year,month)
		if cal[0][0]:
			counter += 1
	return counter

#let the total number of sundays be 0
total = 0

#counting the sundays that fell on 
#first of every month for each year
for i in xrange(1901,2001):
	total += sundays(i)

#time at the end of execution
end = time.time()

#printing the output along with exection time
print "Found {} in {} seconds".format(total,end-start)
