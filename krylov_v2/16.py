import sys

sys.setrecursionlimit(500000)

def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return n*f(n-1)
print(((f(3000)//150)+f(2999))//f(2998))