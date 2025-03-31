def permutation(arr):
    ans =[]
    def backtrack(index):
        if len(arr) == index:
            ans.append(arr[:])
            return
        
        for i in range(index, len(arr)):
            arr[index], arr[i] = arr[i], arr[index]
            backtrack(index+1)
            arr[index], arr[i] = arr[i], arr[index]
    
    backtrack(0)
    return ans

arr = [1,2,3]
print(permutation(arr))