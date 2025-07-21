"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""

def longestPalindrome(s):
    n = len(s)
    def longestPal(left, right):
        while left>=0 and right < n and s[left] == s[right]:
            left = left - 1
            right = right + 1
        return s[left+1: right]
    
    longest = ""
    for i in range(n):
        p1 = longestPal(i, i)
        p2 = longestPal(i, i+1)
        if len(p1)> len(longest):
            longest = p1
        if len(p2)> len(longest):
            longest = p2
    return longest

s = "babad"
print(longestPalindrome(s))