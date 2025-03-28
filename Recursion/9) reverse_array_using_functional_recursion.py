def reverseArray(arr,i,n):
    if i>=n/2:
        return arr
    else:
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
        return reverseArray(arr,i+1,n)

arr = [1,2,3,4,5]
n = 5
i = 0
arr = reverseArray(arr,i,n)
print(arr)
