def f(n, x):
    res = ''
    while n > 0:
        res = str(n % x) + res
        n //= x
    return res

def f1(n):
    r = f(n, 3)
    if n % 3 == 0:
        r = r + r[-2:]
    else:
        z = sum([int(x) for x in r])
        r = r + f(z, 3)

    return int(r, 3)

a = []
for n in range(1, 220):
    a.append(f1(n))
a.sort()
print([x for x in a if x > 220])