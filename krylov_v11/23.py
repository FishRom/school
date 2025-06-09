def f(n, k):
    if n < k or n == 10:
        return 0
    if n == k:
        return 1
    else:
        return f(n-1, k)+f(n//2, k)
print(f(50, 20)*f(20, 1))