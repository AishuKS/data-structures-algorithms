"""
Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

def maxProduct(nums):
    n = len(nums)
    maxDP = [0] * n
    minDP = [0] * n
    maxDP[0] = minDP[0] = result = nums[0]
    for i in range(1,n):
        maxDP[i] = max(nums[i], maxDP[i-1]*nums[i], minDP[i-1]*nums[i])
        minDP[i] = min(nums[i], maxDP[i-1]*nums[i], minDP[i-1]*nums[i])
        result = max(result, maxDP[i])
    return result

nums = [2,3,-2,4]
print(maxProduct(nums))
