def f(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + f(n - 1)
    else:
        return f(n-1) + 2*f(n-2)

print(f(19))