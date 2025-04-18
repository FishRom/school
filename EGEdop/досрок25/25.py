def f(n):
    a = []
    for x in range(2, int(n**0.5)+ 1):
        if n%x == 0:
            a.append(x)
            a.append(n//x)
    return min([x for x in a if x > 7 and x % 10 == 7], default=0)
for i in range(1_125_000, 1_125_100):
    z = f(i)
    if z > 0:
        print(i, z)