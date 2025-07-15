"""
Given a square matrix mat[][], where each cell can be either 'X' or 'O', you need to find the size of the 
largest square subgrid that is completely surrounded by 'X'. More formally you need to find the largest square 
within the grid where all its border cells are 'X'.

Examples:

Input: mat[][] = [[X,X],[X,X]]
Output: 2
Explanation: The largest square submatrix surrounded by X is the whole input matrix.

Input: mat[][] = [[X,X,X,O],[X,O,X,X],[X,X,X,O],[X,O,X,X]]
Output: 3
Explanation:
Here,the input represents following 
matrix of size 4 x 4
X X X O
X O X X
X X X O
X O X X
The square submatrix starting at (0,0) and ending at (2,2) is the largest submatrix surrounded by X. Therefore, size of that matrix would be 3.
"""
mat = [ ['X', 'O', 'X', 'X', 'X'],
                               ['X', 'X', 'X', 'X', 'X'],
                               ['X', 'X', 'O', 'X', 'O'],
                               ['X', 'X', 'X', 'X', 'X'],
                               ['X', 'X', 'X', 'O', 'O'] ]

n = len(mat)
m = len(mat[0])
hor = [[0]*m for i in range(n)]
ver = [[0]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        if mat[i][j] == 'X':
            hor[i][j] = 1 if j == 0 else hor[i][j-1]+1
            ver[i][j] = 1 if i == 0 else ver[i-1][j]+1

maxSize = 0
for i in range(n-1,-1,-1):
    
    for j in range(m-1,-1,-1):
        small = min(hor[i][j], ver[i][j])
        while small > maxSize:
            if hor[i-small+1][j] >= small and ver[i][j-small+1] >= small:
                maxSize = small
            small = small - 1
print(maxSize)