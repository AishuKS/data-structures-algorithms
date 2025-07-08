"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

# Counting Sort - Method 1
from collections import defaultdict


def findKthLargest(nums, k):
    hashMap = defaultdict(int)
    for num in nums:
        hashMap[num] += 1

    min_val, max_val = min(nums), max(nums)
    print(min_val, max_val)
    bucket_size = max_val - min_val + 1
    bucket = [0] * bucket_size

    for num, freq in hashMap.items():
        bucket[num - min_val] = freq

    for i in range(bucket_size - 1, -1, -1):
        while bucket[i]:
            k -= 1
            if k == 0:
                return i + min_val
            bucket[i] -= 1
            
nums = [99,99]
k = 1
print(findKthLargest(nums, k))


#MIN_HEAP - METHOD 2
import heapq

def findKthLargest(nums, k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]
nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums, k))