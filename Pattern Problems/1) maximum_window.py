arr = [1,3,-1,-3,5,3,7,1,6]
k = 15
n = len(arr)
l, r = 0, 0
sum = 0
maxLen = 0
while r<n:
    sum = sum + arr[r]
    while sum > k:
        sum = sum - arr[l]
        l = l + 1
    if sum <= k:
        maxLen = max(maxLen, r-l+1)
    r = r + 1
print(maxLen)
