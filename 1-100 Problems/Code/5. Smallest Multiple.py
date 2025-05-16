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
    num = 1
    prime = {}
    for i in range(2, n+1):
        if isprime(i):
            prime[i] = 1
        else:
            k = i
            for j in prime.keys():
                temp = 0
                while k%j == 0:
                    temp += 1
                    k //= j

                prime[j] = max(temp, prime[j])
    print(prime)
    for i, j in prime.items():
        num *= i**j
    return num

print(solve(int(input())))