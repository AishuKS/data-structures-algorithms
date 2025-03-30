'''

Array of elements and target are given. Give a list of unique combination of array elements, 
where the chosen numbers sum to the target. The combination can be in any order. Each element must be used  
only once

Input: arr = [10,1,2,7,6,1,5], 
target = 7
Output: [[2,2,3],[7]]

'''

def combinationSum(arr, target):
    ans = []
    ds = []
    arr.sort()
    
    def subsequence(ind, target):
        if target == 0:
            ans.append(ds[:])
            return

        for i in range(ind, len(arr)):
            if i>ind and arr[i] == arr[i-1]:
                continue
            if target<arr[i]:
                break
            ds.append(arr[i])
            subsequence(i+1, target-arr[i])
            ds.pop()
            
    subsequence(0,target)
    return ans
    
arr = [2,1,1,3,7]
target = 7
print(combinationSum(arr, target))