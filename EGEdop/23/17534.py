def f(n, k):
    if n < k:
        return 0
    if n == k:
        return 1
    else:
        return f(n - 1, k) + f(n//2, k)

print(f(30, 8) * f(8, 1))
