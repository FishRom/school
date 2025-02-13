def f(n, x):
    res = ''
    while n > 0:
        res = str(n%x) + res
        n //= x
    return res

def f1(n):
    r = f(n, 3)
    if n % 3 == 0:
        r = r + r[-2:]
    else:
        z = f((n%3) * 5, 3)
        r = r + z
    return int(r, 3)
#print(f1(11))

a = []
for n in range(1, 200):
    a.append(f1(n))
#a.sort()
#print(a)
print(min([x for x in a if x > 133]))
