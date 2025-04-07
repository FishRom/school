def f(n):
    res = []
    for x in range(2, int(n**0.5)+1):
        if n%x == 0:
            res.append(x)
            if x < n//x:
                res.append(n//x)
    return min([x for x in res if x > 9 and x%10 == 9], default=0)

#print(f(39))
for c in range(800_001, 800_100):
    z = f(c)
    if z > 0:
        print(c, z)