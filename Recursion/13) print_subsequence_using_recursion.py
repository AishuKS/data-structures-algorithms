def subsequence(arr, index, current):
    if index == len(arr):
        print(current)
        return
    
    subsequence(arr, index+1, current + [arr[index]])
    subsequence(arr, index+1, current)

arr = [3,1,2]
subsequence(arr, 0, [])