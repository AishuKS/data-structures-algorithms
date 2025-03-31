def permuation(arr):
    ans = []
    ds = []
    hash = [False] * len(arr)
    
    def backtrack():
        if len(ds) == len(arr):
            ans.append(ds[:])
            return
        
        for i in range(len(arr)):
            if not hash[i]:
                hash[i] = True
                ds.append(arr[i])
                backtrack()
                ds.pop()
                hash[i] = False
    backtrack()
    return ans

arr = [1,2,3]
print(permuation(arr))
                