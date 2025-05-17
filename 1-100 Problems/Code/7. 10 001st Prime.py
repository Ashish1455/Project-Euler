def isprime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x%2 == 0:
        return False
    for i in range(3, int(x**0.5)+1, 2):
        if x%i == 0:
            return False
    return True

def solve(n):
    if n == 1:
        return 2
    i = 3
    n -= 1
    while n > 0:
        if isprime(i):
            n -= 1
        i += 2
    return i - 2

print(solve(int(input())))