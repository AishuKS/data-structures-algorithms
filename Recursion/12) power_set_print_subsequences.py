s = 'abc'
n = len(s)
for i in range(1,(2**n)):
    substring = ''
    for j in range(n):
        if (i & (1<<j)) > 0:
            substring = substring + s[j]
    print(substring)

