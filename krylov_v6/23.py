def f(n, k):
    if n > k or n == 18:
        return 0
    if n == k:
        return 1
    else:
        return f(n+1, k)+f(n+4, k)+f(n*2, k)
print(f(4, 11)*f(11, 28))