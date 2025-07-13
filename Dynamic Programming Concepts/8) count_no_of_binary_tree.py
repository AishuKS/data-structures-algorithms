"""
Given an integer n, return the number of structurally unique BST's (binary search trees) which has 
exactly n nodes of unique values from 1 to n.

Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1
"""

#USING DYNAMIC PROGRAMMING
nums = [10,11,9,12,13,14]
n = len(nums)

dp = [0] * (n+1)
dp[0] = dp[1] = 1

for i in range(2, n+1):
    for j in range(i):
        dp[i] += dp[j] * dp[i-j-1]
        print("For i = ",i,"j = ",j)
        print(dp)
    print()
print(dp[n])

#USING CATALAN NUMBERS
import math
print(math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n)))