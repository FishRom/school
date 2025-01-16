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
    #print(int(r, 3))
    return int(r, 3)

y = []
for n in range(1, 220):
    y.append(f1(n))
y.sort()
print([x for x in y if x > 220])