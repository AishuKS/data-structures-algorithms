"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def lengthOfLongestSubstring(s):
    string = set()
    count = 0
    left = 0
    for i in range(len(s)):
        while s[i] in string:
            string.remove(s[left])
            left = left + 1
        string.add(s[i])
        count = max(count, i-left + 1)
    return count

s = "abcabcbb"
print(lengthOfLongestSubstring(s))