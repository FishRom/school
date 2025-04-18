def f(n, k):
    if n > k or n == 35:
        return 0
    elif n == k:
        return 1
    else:
        return f(n+1, k)+f(n+2, k)+f(n*2, k)

print(f(7, 13)*f(13, 15)*f(15, 51))