"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the 
non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""

def moveZeroes(nums):
    left = 0
    for i in range(1, len(nums)):
        if nums[left]==0 and nums[i]!=0:
            nums[left] = nums[i]
            left = left + 1
            nums[i] = 0
        if nums[left]!=0:
            left = left + 1
    return nums

nums = [0,1,0,3,12]
print(moveZeroes(nums))