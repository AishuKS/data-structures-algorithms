def count_set_bits(n: int) -> int:
    count = 0
    while n:
        n = n & (n - 1) 
        print(n)
        count += 1
    return count

n = 4
print(count_set_bits(n))