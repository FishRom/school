import sys

sys.setrecursionlimit(5000)

def f(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + 3*f(n-1)
    else:
        return 2 + 2*f(n-2)

print(f(23))