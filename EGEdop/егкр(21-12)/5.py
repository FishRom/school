def f(n):
    res = ''
    while n > 0:
        res = str(n % 3) + res
        n //= 3
    return res

def f1(n):
    r = f(n)
    if n % 3 == 0:
        r = r + r[-2:]
    else:
        z = sum([int(x) for x in r])
        r = r + f(z)
    return int(r, 3)

b = []
for i in range(1, 220):
    b.append(f1(i))
print(min([x for x in b if x > 220 and x % 2 == 0]))