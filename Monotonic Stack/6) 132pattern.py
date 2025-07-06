"""
Given an array of n integers nums, a 132 pattern is a subsequence of three integers 
nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
Return true if there is a 132 pattern in nums, otherwise, return false.

Example 1:
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""

def find132pattern(nums):
    stack = []
    third = float('-inf')
    for i in range(len(nums)-1,-1,-1):
        if nums[i] < third:
            return True
        while stack and nums[i] > stack[-1]:
            third = stack.pop()
        stack.append(nums[i])
    return False

nums = [3,1,4,2]
print(find132pattern(nums))