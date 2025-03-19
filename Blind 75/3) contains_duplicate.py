def containsDuplicate(arr):
    hash = {}
    for i in arr:
        if i in hash:
            return True
        else:
            hash[i] = 1
    return False

arr = [1,2,3,4,1]
print(containsDuplicate(arr))