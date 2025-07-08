"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the 
answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

from collections import defaultdict

def topKFrequent(nums, k):
    hashMap = defaultdict(int)
    for i in nums:
        hashMap[i]+=1
    
    bucket = [[] for i in range(len(nums)+1)]
    result = []

    for key, value in hashMap.items():
        bucket[value].append(key)
    
    for i in range(len(bucket)-1,-1,-1):
        value = bucket[i]
        while value:
            result.append(value.pop())
            if len(result) == k:
                return result
    return result

nums = [1,1,1,2,2,3]
k = 2

print(topKFrequent(nums, k))