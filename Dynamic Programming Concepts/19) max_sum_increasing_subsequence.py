"""
Given an array of positive integers arr. Find the maximum sum subsequence of the given array such 
that the integers in the subsequence are sorted in strictly increasing order i.e. a strictly increasing 
subsequence. 

Examples:

Input: arr[] = [1, 101, 2, 3, 100]
Output: 106
Explanation: The maximum sum of a increasing sequence is obtained from [1, 2, 3, 100].

Input: arr[] = [4, 1, 2, 3]
Output: 6
Explanation: The maximum sum of a increasing sequence is obtained from {1, 2, 3}.

Input: arr[] = [4, 1, 2, 4]
Output: 7
Explanation: The maximum sum of a increasing sequence is obtained from {1, 2, 4}.
"""

def maxSumIS(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(n):
        dp[i] = arr[i]
    for i in range(1,n):
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i] = max(dp[i], dp[j]+arr[i])
    return max(dp)

arr = [5,3,2,4,7,9,8,2,3]
print(maxSumIS(arr))