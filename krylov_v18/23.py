def f(n, k):
    if n < k:
        return 0
    elif n == k:
        return 1
    else:
        return f(n - 1, k)+f(n // 2, k)
print(f(31, 12)*f(12, 2))