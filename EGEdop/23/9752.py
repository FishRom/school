def f(n, k):
    if n > k or n == 17:
        return 0
    if n == k:
        return 1
    else:
        return f(n+2, k) + f(n+3, k) + f(n*2, k)

print(f(3, 10) * f(10, 25))