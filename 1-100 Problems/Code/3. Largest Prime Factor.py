def isprime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

def solve(n):
    factor = 2
    last = 1
    while factor*factor <= n:
        if n%factor == 0:
            if isprime(factor):
                last = factor
            n //= factor
            print(last)
        else:
            factor += 1 if factor == 2 else 2
    return max(n, last)
        
print(solve(int(input())))