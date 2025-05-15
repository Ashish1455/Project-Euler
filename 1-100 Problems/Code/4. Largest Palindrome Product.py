def palindrome(n):
    x = n
    n2 = 0
    while x != 0:
        temp = x%10
        n2 = n2*10 + temp
        x //= 10
    return n2 == n

x = 999
maxnum = 0
for i in range(x, 99, -1):
    for j in range(x, 99, -1):
        if i*j <= maxnum:
            break
        if palindrome(i*j):
            maxnum = max(maxnum, i*j)
print(maxnum)