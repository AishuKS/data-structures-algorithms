'''

Array of elements are given. Return all possible subset without duplications but can be in any order. 

Input: arr = [1, 2, 2] 
Output: [[1, 2], [2], [1], [1, 2, 2], [2, 2], []]

'''

def subDup(arr):
    ans = set()
    def subset(arr, index, current):
        if len(arr) == index:
            ans.add(tuple(current))
            return
        
        current.append(arr[index])
        subset(arr, index+1, current)
        current.pop()
        subset(arr, index+1, current)
    
    subset(arr, 0, [])
    arr.sort()
    return [list(t) for t in ans]

arr = [1,2,2]
print(subDup(arr))