import sys

sys.setrecursionlimit(50000)

def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return n*f(n-1)

print(((f(2025)//25) + f(2024)) / f(2023))