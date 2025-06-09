def f(n, k):
    if n > k or n == 17 or n == 11:
        return 0
    elif n == k:
        return 1
    else:
        return f(n+1, k)+f(n+4, k)+f(n*2, k)
print(f(3, 24))