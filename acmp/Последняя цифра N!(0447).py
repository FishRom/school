def find_last_nonzero_digit(n):
    last_nonzero_digit = 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        while factorial % 10 == 0:
            factorial //= 10
        last_nonzero_digit = factorial % 10
    return last_nonzero_digit

n = int(input())
last_nonzero_digit = find_last_nonzero_digit(n)
print(last_nonzero_digit)