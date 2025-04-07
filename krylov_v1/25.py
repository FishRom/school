def f(n):
    a = []
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            a.append(x)
            if x != n//x:
                a.append(n//x)
    z = min([x for x in a if x % 10 == 7 and x > 7], default=0)
    return z

for h in range(700_001, 701_000):
    if f(h) > 0:
        print(h, f(h))
