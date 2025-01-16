def f(n, x):
    res = ''
    while n > 0:
        res = str(n % x) + res
        n //= x
    return res

def f1(n):
    r = f(n, 3)
    if n % 3 == 0:
        r = '1' + r + '01'
    else:
        z = f((n%3)*4, 3)
        r = r + z
    return int(r, 3)

a = []
for n in range(1, 200):
    if f1(n) < 199:
        a.append(n)
print(max(a))