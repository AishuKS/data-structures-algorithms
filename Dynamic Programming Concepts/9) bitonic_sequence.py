"""
Given an array of positive integers. Find the maximum length of Bitonic subsequence. 
A subsequence of array is called Bitonic if it is first strictly increasing, then strictly decreasing. 
Return the maximum length of bitonic subsequence. 
Note : A strictly increasing or a strictly decreasing sequence should not be considered as a bitonic sequence

Examples :

Input: n = 5, nums[] = [1, 2, 5, 3, 2]
Output: 5
Explanation: The sequence {1, 2, 5} is increasing and the sequence {3, 2} is decreasing so 
merging both we will get length 5.

Input: n = 8, nums[] = [1, 11, 2, 10, 4, 5, 2, 1]
Output: 6
Explanation: The bitonic sequence {1, 2, 10, 4, 2, 1} has length 6.

Input: n = 3, nums[] = [10, 20, 30]
Output: 0
Explanation: The decreasing or increasing part cannot be empty

Input: n = 3, nums[] = [10, 10, 10]
Output: 0
Explanation: The subsequences must be strictly increasing or decreasing
"""
nums = [1, 11, 2, 10, 4, 5, 2, 1]
nums = [1, 2, 3, 4, 5]
nums = [1, 2, 5, 3, 2]
nums = [6, 4, 2, 2, 1, 8, 3, 1, 10]
n = len(nums)
r1 = [1] * (n)
r2 = [1] * (n)

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            r1[i] = max(r1[i], r1[j]+1)
    
for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        if nums[i] > nums[j]:
            r2[i] = max(r2[i], r2[j]+1)

maxLen = 0
for i in range(n):
    if r1[i] > 1 and r2[i] > 1:
        maxLen = max(maxLen, r1[i]+r2[i]-1)

print(maxLen)