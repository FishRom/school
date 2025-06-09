def f(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i + n//i
    return 0

for x in range(800_001, 800_101):
    if f(x) % 10 == 6:
        print(x, f(x))