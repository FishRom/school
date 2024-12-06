def f(n):
    res = 0
    a = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            a.append(i)
            a.append(n//i)
    res = min([x for x in a if x > 9 and x % 10 == 9], default=0)
    return res

res = 0
for i in range(800001, 800100):
    z = f(i)
    if z > 0:
        print(i, z)
        res += 1
    if res == 5:
        break