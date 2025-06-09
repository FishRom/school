def f(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return n//i - i
    return 0

for x in range(850_001, 850_101):
    if f(x) % 5 == 0 and f(x) > 0:
        print(x, f(x))