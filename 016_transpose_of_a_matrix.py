'''
Program to find transpose of a matrix

Given a 2D matrix mat[][], compute its transpose. The transpose of a matrix is formed by converting all rows of mat[][] into columns and all columns into rows.

Example:

Input: mat[][]=[[1, 1, 1, 1],
                [2, 2, 2, 2],
                [3, 3, 3, 3],
                [4, 4, 4, 4]]
Output:[[1, 2, 3 ,4],
        [1, 2, 3, 4],
        [1, 2, 3, 4],  
        [1, 2, 3, 4]]
Explanation:  The output is the transpose of the input matrix, where each row becomes a column. This rearranges the data so that vertical patterns in the original matrix become horizontal in the result.

Input: mat[][] = [[1, 2],
                  [9, -2]]
Output: [[1, 9],
         [2, -2]]
Explanation:  The output is the transpose of the input matrix, where each row becomes a column. This rearranges the data so that vertical patterns in the original matrix become horizontal in the result.
'''
'''
Algorithm:
create a transpose matrix with 1s
replace vales with vales from real matrix
'''
mat=[[1, 1, 1, 1],
     [2, 2, 2, 2],
     [3, 3, 3, 3],
     [4, 4, 4, 4]]

m,n = len(mat),len(mat[0])
transpose =[[0]*m for i in range(n)]
for i in range(m):
    for j in range(n):
        transpose[i][j] = mat[j][i]

print(transpose)
