'''

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

 
Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt (right click and "Save Link/Target As..."), 
a 31K text file containing an 80 by 80 matrix.

# https://projecteuler.net/project/resources/p081_matrix.txt

'''
m = [map(int, row.split(',')) for row in open("tps://projecteuler.net/project/resources/p081_matrix.txt").readlines()]
c, r = len(m), len(m[0])

for i in xrange(1,c):
    for j in xrange(1,r):
        m[i][0]+= m[i-1][0]
        m[0][j]+= m[0][j-1]
        m[i][j]+= min(m[i-1][j], m[i][j-1])
 
print "Minimal path sum in", r, "by", c, "matrix =", m[-1][-1]
