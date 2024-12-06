def f(n, k):
    if n > k or n == 16:
        return 0
    elif n == k:
        return 1
    else:
        return f(n + 1, k) + f(n + 2, k) + f(n * 3, k)

print(f(2, 9) * f(9, 18))