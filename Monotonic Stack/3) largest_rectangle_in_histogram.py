"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
"""
def largestRectangleArea(heights):
    stack = []  # stores indices
    max_area = 0
    heights.append(0)  # Add sentinel to flush the stack at the end

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
            print(max_area, height, i)
        stack.append(i)

    return max_area

heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))