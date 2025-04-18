def f(n):
    r = []
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            if (i + n//i)%10 == 6:
                return i + n//i
            else:
                return 0
    return 0

for x in range(1_000_001, 1_000_101):
    z = f(x)
    if z > 0:
        print(x, z)