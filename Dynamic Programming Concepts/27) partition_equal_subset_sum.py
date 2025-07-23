"""
Given an integer array nums, return true if you can partition the array into two subsets such 
that the sum of the elements in both subsets is equal or false otherwise.

Example 1:
Input: nums = [1,5,11,5]
Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""

def canPartition(nums):
    total = sum(nums)
    if total%2 != 0:
        return False
    target = total // 2
    dp = [False] * (target+1)
    dp[0] = True
    for num in nums:
        for j in range(target, num-1,-1):
            dp[j] = dp[j] or dp[j-num]
        if dp[target]:
            return True
    return False

nums = [1,5,11,5]

print(canPartition(nums))