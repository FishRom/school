def f(n):
    res = []
    for x in range(2, int(n**0.5) + 1):
        if n%x == 0:
            res.append(x)
            if x < n//x:
                res.append(n//x)
    return (sum(res))


for i in range(500001, 500150):
    z = f(i)
    if z%10 == 9:
        print(i, z)