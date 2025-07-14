"""
Given a positive integer n, count all possible distinct binary strings of length n such that 
there are no consecutive 1’s.

Examples :
Input: n = 3
Output: 5
Explanation: 5 strings are ("000", "001", "010", "100", "101").

Input: n = 2
Output: 3
Explanation: 3 strings are ("00", "01", "10").

Input: n = 1
Output: 2
"""
def countStrings(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    dp = [1] * n
    dp[0] = 2
    dp[1] = 3
    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]

n = 5
print(countStrings(n))