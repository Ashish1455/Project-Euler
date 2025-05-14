def solve():
    fib_sum = 0
    fib = [1, 2]
    while fib[1] < 4000000:
        if fib[1]%2 == 0:
            fib_sum += fib[1]
        fib[0], fib[1] = fib[1], fib[0] + fib[1]
    return fib_sum

print(solve())