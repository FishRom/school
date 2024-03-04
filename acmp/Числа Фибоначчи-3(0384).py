def nod(a,  b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
def fib(n):
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, (a + b) % 1000000000
    return b
a, b = map(int, input().split())
print(fib(nod(a, b)))
