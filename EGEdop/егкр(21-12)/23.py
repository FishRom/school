def f(n, k):
    if n < k or n == 24:
        return 0
    elif n == k:
        return 1
    else:
        return f(n-1, k) + f(n-6, k) + f(n//2, k)
print(f(34, 29)*f(29, 19)*f(19, 6))
