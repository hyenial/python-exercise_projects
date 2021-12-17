'''
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, 
by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

 
Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
'''
def four_way(matrix):

    """Computes the minimum path sum from the top left to the bottom right of a matrix
    by only moving to the left, right, up and down. Uses Dijkstra's Algorithm"""

    n = len(matrix)

    current = (0,0)
    permanent = {current: weight(current)}   #permanent[node] = minimum path sum from (0, 0) to node
    temporary = {}   #temporary nodes waiting to be made permanent
    total_nodes = n*n
    
    while len(permanent) < total_nodes:
        for node in neighbours(current, n):     #iterating over all possible moves from current node
            if not (node in permanent):      #so long as the node has not already been made permanent
                if node in temporary:        #if the node has been visited previously
                    if temporary[node] > permanent[current] + weight(node):  #update temporary path only if new path is smaller
                         temporary[node] = permanent[current] + weight(node)
                else:
                    temporary[node] = permanent[current] + weight(node)  #if the node has not been visited previously, create temporary path

        min_weight = min(temporary.values())    #minimum path over all temporary nodes
        min_nodes = [node for node in temporary if temporary[node]==min_weight]   #all nodes with the minimum path - there may be more than one
        min_node = min_nodes[0]  #arbitrarily select one of the nodes
        permanent[min_node] = min_weight
        del temporary[min_node]
        current = min_node

    return permanent[(n-1),(n-1)]

def neighbours(tuple, n):
    
    """Returns matrix indices of all possible moves from the node 'tuple'"""

    i = tuple[0]
    j = tuple[1]
    moves = [(i+x, j+y) for x, y in [(-1,0), (0, -1), (1, 0), (0, 1)]
             if 0 <= i+x < n and 0 <= j+y < n]
    
    return moves
    
def weight(tuple):
    
    """Returns the weight of node 'tuple'"""
    
    i = tuple[0]
    j = tuple[1]
    return matrix[i][j]

if __name__ == '__main__':
    
    matrix = [[int(v) for v in line.strip().split(',')] for line in open('matrix.txt','r')]
    print(four_way(matrix))
