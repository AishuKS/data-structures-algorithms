"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""

def minPathSum(grid):

    row = len(grid)
    col = len(grid[0])

    for i in range(1,col):
        grid[0][i] = grid[0][i-1] + grid[0][i]

    for i in range(1, row):
        grid[i][0] = grid[i-1][0] + grid[i][0]
    
    for i in range(1, row):
        for j in range(1, col):
            grid[i][j] = min((grid[i][j]+grid[i-1][j]), (grid[i][j]+grid[i][j-1]))

    return grid[row-1][col-1]

grid = [[1,2,3],[4,5,6]]
print(minPathSum(grid))