def f(n):
    res = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            res.append(i)
            if i < n//i:
                res.append(n//i)
    return min([x for x in res if x % 1000 == 777], default=0)

for x in range(55_000_001, 55_001_001):
    if f(x) > 0:
        print(x, f(x))

#?????????????????????????????