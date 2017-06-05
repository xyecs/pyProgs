def isPalindrome(s):
    t = s[::-1]
    if t == s:
        return True
    return False

palindromes = []
a = 999
b = 999

for i in range(999, 0, -1):
    for j in range(999, 0, -1):
        c = i * j
        if isPalindrome(str(c)):
            palindromes.append(c)

print max(palindromes)
