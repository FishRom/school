def f(n, k):
    if n > k or n == 35:
        return 0
    if n == k:
        return 1
    else:
        return f(n+1, k) + f(n+2, k)+ f(n+4, k)

print(f(24, 33)*f(33, 42))