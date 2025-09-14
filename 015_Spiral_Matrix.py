'''
Spiral Matrix

Given a matrix mat[][] of size m x n, the task is to print all elements of the matrix in spiral form

Examples: 

Input: mat[][]=[[1,   2,   3,   4],
                [5,    6,   7,   8],
                [9,   10,  11,  12],
                [13,  14,  15,  16]]
Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
 
Input: mat[][]=[[1,   2,   3,   4,  5,   6],
                [7,   8,   9,  10,  11,  12],
                [13,  14,  15, 16,  17,  18]]

Output: [1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7, 8, 9, 10, 11]
'''
'''
Algorithm:
while top<=bottom and left<=right:
    Left → Right (top row)
    top+1
    Top → Bottom (right column)
    right-1
    Right → Left (bottom row)
    bottom -1
    Bottom → Top (left column)
    left -1
'''

mat =   [[1,   2,   3,   4,  5,   6],
                [7,   8,   9,  10,  11,  12],
                [13,  14,  15, 16,  17,  18]]

m,n = len(mat),len(mat[0])
top , bottom = 0,m-1
left, right = 0, n-1
res = []

while top<=bottom and left<=right:
    for j in range(left,right+1):
        res.append(mat[top][j])
    top+=1
    for i in range(top,bottom+1):
        res.append(mat[i][right])
    right-=1
    if top <= bottom:
        for j in range(right,left-1,-1):
            res.append(mat[bottom][j])
        bottom-=1
    if left <= right:
        for i in range(bottom,top-1,-1):
            res.append(mat[i][left])
        left+=1

print(res)
    
