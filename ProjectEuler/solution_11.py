"""

In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

"""
#As the matrix is in string format
#First we are splitting it row wise
numbers = numbers.strip().split('\n')

#Once split row wise we are splitting it column wise also
#We are also converting the
#the items in matrix to int using map
numbers = [map(int,x.strip().split(' ')) for x in numbers]


def greatest_product(a):
	"""
	This function will take a matrix as input and then output
	the largest product that is possible in the Matrix
	Example: Consider
	a = [[40, 62, 76, 36],
	 	 [74, 04, 36, 16],
	 	 [23, 57, 05, 54],
	 	 [89, 19, 67, 48]]
	 ""ROW WISE CALCULATIONS""	 
	 In the first for loop we are calculating the values of
	 40*62*76*36, 74*04*36*16, 23*57*05*54,89*19*67*48
	 using iterations and then for every value generated 
	 we are checking if the value of the multiple is 
	 greater than 'largest'. If yes change its value
	 ""COLUMN WISE CALCULATIONS""
	 In the second for loop we are calculating the values of
	 40*74*23*89, 62*04*57*19, 76*36*05*67, 36*16*54*48
	 and if any of these values is greater than the 
	 'largest' value then we will change it.
	 ""DIAGONAL CALCULATIONS""
	 In the third for loop, the diagonal calculations are 
	 40*04*05*48, 36*36*57*89.
	 If any of the values is greater than the previous value 
	 of 'largest' then it will be changed
	 Finally the value of largest is returned
	"""
	largest = 0
	for i in a:
		multiple = reduce(lambda x,y:x*y,i)
		if multiple > largest:
			largest = multiple
	for j in xrange(len(a)):
		multiple = 1
		for k in xrange(len(a)):
			multiple = multiple*a[k][j]
		if multiple > largest:
			largest = multiple
	multiple = 1
	right_dia = 1
	for k in xrange(len(a)):
		multiple = multiple*a[k][k]
		right_dia *= a[len(a)-1-k][k]
	if multiple > largest:
		largest = multiple
	if right_dia > largest:
		largest = right_dia
	return largest

#A list to store the values of sub matrices
a = []

#For loop for generating sub matrices
#Try to understand this by considering a small
#example similar to the function above.
for i in range(len(numbers)-3):
	for j in range(len(numbers[0])-3):
		sub = []
		sub.append(numbers[i][j:j+4])
		sub.append(numbers[i+1][j:j+4])
		sub.append(numbers[i+2][j:j+4])
		sub.append(numbers[i+3][j:j+4])
		a.append(sub)

#Applying the greatest_product function 
# to all of the sub matrices
a = map(greatest_product,a)

#printing the biggest number in the list
print max(a)

#Total time taken for execution
print time.time() - start

# referance : https://gist.github.com/Anivarth/26fef0a19ebe9ad58754b90e61193b0f
# thank you Anivarth
