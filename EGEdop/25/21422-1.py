def f(n):
    res = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            res.append(i)
            if i < n//i:
                res.append(n//i)
    return min([x for x in res if x % 10 == 7 and x > 7], default=0)

for x in range(1_125_001, 1_125_101):
    r = f(x)
    if r > 0:
        print(x, r)