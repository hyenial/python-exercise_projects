
'''

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, 
and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

 
Find the minimal path sum from the left column to the right column in matrix.txt 
(https://projecteuler.net/project/resources/p081_matrix.txt."),
a 31K text file containing an 80 by 80 matrix.

referance : https://github.com/t-cousins/Project-Euler-82/blob/master/three_way.py
'''
def three_way(matrix):
    """Computes the minimum path sum from any cell in the first column to any cell in the
    last column of a matrix by only moving to the right, up and down"""

    n = len(matrix)
    
    #q[i][j] = minimum cost to reach any cell in the last column from (i,j)
    q = [[0 for c in range(n)] for r in range(n)]   #initialise q with zeros
    
    for i in range(n):           #fill last column of q with last column of matrix
        q[i][n-1] = matrix[i][n-1]
    
    for j in range(n-2, -1, -1):    #filling in the columns of q backwards
        
        #up_or_right[i] = minimum cost to reach any cell in the last column from [i,j] by first moving up or right to column [j+1] 
        up_or_right = [0 for c in range(n)]
        up_or_right[0] = matrix[0][j] + q[0][j+1]    #top cell in column can only move right

        for i in range(1,n):      #iterating down each column
            up_or_right[i] = min(matrix[i][j] + up_or_right[i-1], #moving up
                                 matrix[i][j] + q[i][j+1])  #moving right

        q[n-1][j] = up_or_right[n-1]   #bottom cell cannot go down 

        for i in range(n-2, -1, -1):    #iterating up each column
            q[i][j] = min(up_or_right[i],   #up or right
                           matrix[i][j] + q[i+1][j])    #first going down
    
   
    return min([q[i][0] for i in range(n)])   # minimum value in first column of q 

if __name__ == '__main__':
    matrix = [[int(v) for v in line.strip().split(',')] for line in open('matrix.txt','r')]
    print(three_way(matrix))
