import numpy
game = [
[2,2,1],
[1,1,2],
[1,2,1]]
set_r = ()
set_c = ()
def line_match(game):
	for i in range(3):
		set_r = set(game[i])
		if len(set_r) == 1 and game[i][0] != 0:
			return game[i][0]
	return 0
#transposed column function for future use
#def column(game):
#	trans = numpy.transpose(game)
#	for i in range(3):
#		set_r = set(trans[i])
#		if len(set_r) == 1 and trans[i][0] != 0:
#			return list(set_r)[0]

def diagonal_match(game):
	if game[1][1] != 0:
		if game[1][1] == game[0][0] == game[2][2]: 
			return game[1][1]
		elif game[1][1] == game[0][2] == game[2][0]:
			return game[1][1]			
	return 0
if line_match(game) > 0:			
	print (str(line_match(game)) + str(" row wins!"))
if line_match(numpy.transpose(game)) > 0:
	print (str(line_match(numpy.transpose(game))) + str(" column wins!"))
if diagonal_match(game) > 0:
	print (str(diagonal_match(game)) + str(" diagonal wins!"))
  
 def checkGrid(grid):
	# rows
	for x in range(0,3):
		row = set([grid[x][0],grid[x][1],grid[x][2]])
		if len(row) == 1 and grid[x][0] != 0:
			return grid[x][0]

	# columns
	for x in range(0,3):
		column = set([grid[0][x],grid[1][x],grid[2][x]])
		if len(column) == 1 and grid[0][x] != 0:
			return grid[0][x]

	# diagonals
	diag1 = set([grid[0][0],grid[1][1],grid[2][2]])
	diag2 = set([grid[0][2],grid[1][1],grid[2][0]])
	if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
		return grid[1][1]

	return 0

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

print(checkGrid(also_no_winner))
