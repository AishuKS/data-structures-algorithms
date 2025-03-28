def checkPalindrome(s,i,n):
    if i>=n/2:
        return True
    else:
        if s[i].lower()!=s[n-i-1].lower():
            return False
        else:
            return checkPalindrome(s,i+1,n)
        
s = 'Madam'
n = len(s)
i = 0
ans = checkPalindrome(s,i,n)
print(ans)