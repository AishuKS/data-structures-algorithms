"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""

from cmath import inf


def minSubArrayLen(target, nums):
    left = 0
    value = 0
    count = float(inf)
    for i in range(len(nums)):
        value = value + nums[i]
        while value >= target:
            count = min(count, i-left +1)
            value = value - nums[left]
            left = left + 1
    if count == float(inf):
        return 0
    return count

target = 7
nums = [2,3,1,2,4,3]

print(minSubArrayLen(target, nums))