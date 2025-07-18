"""
Given a string s, find the longest palindromic subsequence's length in s.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements 
without changing the order of the remaining elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb". 
"""

def longestPalindromeSubseq(s):
    n = len(s)
    dp = [[0] * n for i in range(n)]

    for i in range(n-1,-1,-1):
        dp[i][i] = 1
        for j in range(i+1,n):
            if s[i]==s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j-1])
    return dp[0][n-1]

s = "bbbab"
print(longestPalindromeSubseq(s))