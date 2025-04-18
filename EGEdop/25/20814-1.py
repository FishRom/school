def f(n):
    r = []
    for x in range(2, int(n**0.5) + 1):
        if n%x == 0:
            r.append(x)
            if x < n//x:
                r.append(n//x)
    return sum(r)

for i in range(500_001, 500_100):
    z = f(i)
    if z%10 == 9:
        print(i, z)