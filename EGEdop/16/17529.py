import sys

sys.setrecursionlimit(5000)

def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n - 1)

print((2 * f(2024) + f(2023)) / f(2022))