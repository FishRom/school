def f(n):
    res = []
    for x in range(2, int(n ** 0.5)):
        if n % x == 0 and x < n//x:
            return x + n//x
    return 0

for n in range(700_001, 700_100):
    z = f(n)
    if z % 10 == 4:
        print(n, z)