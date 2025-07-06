"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""

def trap(height):
    left = 0
    right = len(height) - 1
    leftMax = 0
    rightMax = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= leftMax:
                leftMax = height[left]
            else:
                water = water + leftMax - height[left] 
            left = left + 1
        else:
            if height[right] >= rightMax:
                rightMax = height[right]
            else:
                water = water + rightMax - height[right]
            right = right - 1
        
    return water

height = [0,1,0,2,1,0,1,3,2,1,2,1]

print(trap(height))