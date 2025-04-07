def f(n, k):
    if n > k:
        return 0
    if n == k:
        return 1
    else:
        return f(n+1, k)+f(n*2, k)+f(n*3, k)
print(f(3, 9)*f(9, 30))

print(700-48)