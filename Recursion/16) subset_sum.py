def subsetSum(arr, index, sum, ans):
    if index == len(arr):
        ans.append(sum)
        sum = 0
        return

    subsetSum(arr, index+1, sum+arr[index], ans)
    subsetSum(arr, index+1, sum, ans)

arr = [3,1,2]
ans = []
subsetSum(arr, 0, 0, ans)
print(ans)