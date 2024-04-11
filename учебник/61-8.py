def g(n):
    if n == 0:
        return
    if n % 3 == 2:
        g((n + 1) // 3)
        print('#', end='')
    else:
        g(n // 3)
        print(n % 3, end='')