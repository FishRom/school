def f(n, k):
    if n < k:
        return 0
    elif n == k:
        return 1
    else:
        return f(n-2, k)+f(n//2, k)

print(f(52, 14)*f(14, 2))