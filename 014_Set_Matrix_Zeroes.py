'''
Set Matrix Zeroes

Given a boolean matrix mat where each cell contains either 0 or 1, the task is to modify it such that if a matrix cell matrix[i][j] is 1 then all the cells in its ith row and jth column will become 1.

Examples:

Input:[[1, 0],
       [0, 0]]
Output:[[1, 1],
        [1, 0]]

Input: [[1, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 0, 0]]
Output:[[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 0, 1, 1]]
'''
'''
Algorithm:
store index of 1 in an temp array
make all 


'''
mat = [[1, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 0, 0]]

m =len(mat)
n = len(mat[1])
rows = set()
columns = set()
for i in range(m):
    for j in range(n):
        if(mat[i][j]==1):
            rows.add(i)
            columns.add(j)

for i in range(m):
    for j in range(n):
        if i in rows  or j in columns:
            mat[i][j] = 1
import numpy as np
print(np.array(mat))
