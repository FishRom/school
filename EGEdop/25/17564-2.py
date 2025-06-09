def f(n):
    for i in range(2, int(n**0.5)+ 1):
        if n % i == 0:
            return i + n//i
    return 0

for x in range(700_001, 700_101):
    if f(x) % 10 == 4:
        print(x, f(x))