def solve(n):
    # return n*((n**2)-1)*(3*n+2)//12
    square_sum = 0
    n_sum = 0
    for i in range(n+1):
        n_sum += i
        square_sum += i**2
    return n_sum**2 - square_sum

print(solve(int(input())))