def f(n):
    res = 0
    a = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            a.append(i)
            a.append(n//i)
    res = min([x for x in a if x % 10 == 7 and x > 7], default=0)
    return res

res = 0
for i in range(700001, 700100):
    z = f(i)
    if z > 0:
        res += 1
        print(i, z)

    if res == 5:
        break