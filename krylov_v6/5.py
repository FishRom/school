def f(n):
    res = ''
    while n >0:
        res = str(n%4) + res
        n //= 4
    return res

def p(n):
    r = f(n)
    if n % 4 == 0:
        r = r + r[-2:]
    else:
        r = r + f((n%4)*2)
    return int(r, 4)

for n in range(1, 500):
    if p(n) < 369:
        print(n)
        