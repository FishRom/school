def f(n):
    res = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            res = n // i + i
            break
    return res

res = 0
for i in range(800001, 800100):
    z = f(i)
    if z % 10 == 4:
        res += 1
        print(i, z)
    if res == 5:
        break