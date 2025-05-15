def solve(x):
    multiples_sum = 0
    for i in range(1,x):
        if i%3 == 0 or i%5 == 0:
            multiples_sum += i
    return multiples_sum

print(solve(int(input())))