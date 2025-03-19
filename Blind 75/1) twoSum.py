input = [2,7,11,15]
target = 9

hash = {}

for i in range(len(input)):
    value = target - input[i]
    if value in hash:
        print (hash[value], i)
        break
    hash[input[i]] = i 