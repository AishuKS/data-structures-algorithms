'''

Distinct number of elements in an array and target are given. Give a list of unique combination of array elements, 
where the chosen numbers sum to the target. The combination can be in any order. Each element can be used any 
number of times,

Input: arr = [2,3,6,7], 
target = 7
Output: [[2,2,3],[7]]

'''

def subsequence (arr, target):
    ds = []
    ans = []
    
    def combination(index, target):
        if len(arr) == index:
            if target == 0:
                ans.append(ds[:])
            return

        if target>=arr[index]:
            ds.append(arr[index])
            combination(index, target-arr[index])
            ds.pop()
        combination(index+1, target)
    
    combination(0, target)
    return ans

arr = [2,3,6,7]
target = 7
print(subsequence(arr,target))