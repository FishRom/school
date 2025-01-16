def f(n, x):
    res = ''
    while n > 0:
        res = str(n % x) + res
        n //= x
    return res

def f1(n):
    r = f(n, 4)
    if n % 4 == 0:
        r = r + r[-2:]
    else:
        z = f((n % 4)*2, 4)
        r = r + z
    return int(r, 4)
print(f1(61))

a = []
for n in range(1, 261):
    if f1(n) < 261:
        a.append(n)
print(max(a))