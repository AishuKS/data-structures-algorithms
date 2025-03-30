'''

Array of elements are given. Return all possible subset without duplications but can be in any order. 

Input: arr = [1, 2, 2] 
Output: [[1, 2], [2], [1], [1, 2, 2], [2, 2], []]

'''


def subsetsWithDup(arr):
    ans = []
    ds = []

    def subsequence(index):
        ans.append(ds[:])

        for i in range(index, len(arr)):
            if i!=index and arr[i] == arr[i-1]:
                continue
            ds.append(arr[i])
            subsequence(i+1)
            ds.pop()

    arr.sort()  # Important to group duplicates
    subsequence(0)
    return ans  # Convert back to list

arr =[1,2,2]
print(subsetsWithDup(arr))