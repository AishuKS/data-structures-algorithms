def findMaxLength(nums):
    count_index = {0: -1}  # prefix_sum : first_index
    max_len = 0
    prefix_sum = 0

    for i, num in enumerate(nums):
        prefix_sum += 1 if num == 1 else -1

        if prefix_sum in count_index:
            max_len = max(max_len, i - count_index[prefix_sum])
        else:
            count_index[prefix_sum] = i

    return max_len

nums = [0,1,1,1,1,1,0,0,0]
print(findMaxLength(nums))