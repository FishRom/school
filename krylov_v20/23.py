def f(n, k):
    if n < k:
        return 0
    elif n == k:
        return 1
    else:
        return f(n-1, k)+f(n//3, k)

print(f(37, 10)*f(10, 2))