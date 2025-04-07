def f(n, k):
    if n > k or n == 23:
        return 0
    elif n == k:
        return 1
    else:
        return f(n+1, k) + f(n+3, k) + f(n*4, k)

print(f(4, 18)*f(18, 35))