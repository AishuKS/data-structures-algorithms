"""
Given a sorted array keys[0.. n-1] of search keys and an array freq[0.. n-1] of frequency counts, where 
freq[i] is the number of searches to keys[i]. Construct a binary search tree of all keys such that the total 
cost of all the searches is as small as possible.
Let us first define the cost of a BST. The cost of a BST node is level of that node multiplied by its frequency. 
Level of root is 1.


Example 1:
Input:
n = 2
keys = {10, 12}
freq = {34, 50}
Output: 118
Explaination:
There can be following two possible BSTs 
        10                       12
          \                     / 
           12                 10
                              
The cost of tree I is 34*1 + 50*2 = 134
The cost of tree II is 50*1 + 34*2 = 118 

Example 2:
Input:
N = 3
keys = {10, 12, 20}
freq = {34, 8, 50}
Output: 142
Explaination: There can be many possible BSTs
     20
    /
   10  
    \
     12  
     
Among all possible BSTs, 
cost of this BST is minimum.  
Cost of this BST is 1*50 + 2*34 + 3*8 = 142
"""


keys = [10, 12, 16, 21]
freq = [4, 2, 6, 3]

n = len(keys)
dp = [[0] * n for i in range(n)]
sum_freq = [0] * (n+1)

# Precompute prefix sum of frequencies
for i in range(n):
    sum_freq[i+1] = sum_freq[i] + freq[i]

# Helper to get sum of freq[i..j]
def get_sum(i, j):
    return sum_freq[j+1] - sum_freq[i]

# Initialize base cases
for i in range(n):
    dp[i][i] = freq[i]

# l is the chain length
for length in range(2, n+1):
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = float('inf')

        # Try making all keys[i..j] as root
        for r in range(i, j + 1):
            cost_left = dp[i][r - 1] if r > i else 0
            cost_right = dp[r + 1][j] if r < j else 0
            total = cost_left + cost_right + get_sum(i, j)
            dp[i][j] = min(dp[i][j], total)
            
print(dp[0][n - 1])
