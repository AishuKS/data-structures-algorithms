"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
"""

from collections import defaultdict


def subarraySum(nums, k):
    hashMap = defaultdict(int)
    hashMap[0] = 1
    value = 0
    result = 0
    for i in range(len(nums)):
        value = value + nums[i]
        target = value - k
        if target in hashMap:
            result = result + hashMap[target]
        hashMap[value]+=1
    return result
