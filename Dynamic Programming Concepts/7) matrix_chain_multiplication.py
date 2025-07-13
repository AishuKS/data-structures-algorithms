"""
Input: arr[] = [2, 1, 3, 4]
Output: 20
Explanation: There are 3 matrices of dimensions 2 × 1, 1 × 3, and 3 × 4, 
Let this 3 input matrices be M1, M2, and M3. There are two ways to multiply: ((M1 x M2) x M3) and 
(M1 x (M2 x M3)), note that the result of (M1 x M2) is a 2 x 3 matrix and result of (M2 x M3) is a 1 x 4 matrix. 
((M1 x M2) x M3)  requires (2 x 1 x 3) + (2 x 3 x 4) = 30 
(M1 x (M2 x M3))  requires (1 x 3 x 4) + (2 x 1 x 4) = 20. 
The minimum of these two is 20.
"""
arr = [2, 3, 6, 4, 5]
n = len(arr) - 1
dp = [[0] * n for i in range(n)]
for length in range(2, n+1):
    for i in range(n-length+1):
        j = i+length-1
        dp[i][j] = float('inf')
        for k in range(i,j):
            cost = dp[i][k] + dp[k+1][j] + arr[i] * arr[k+1] * arr[j+1]
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][n-1], dp)