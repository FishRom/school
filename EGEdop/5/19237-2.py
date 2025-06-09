def tr(n):
    res = ''
    while n > 0:
        res = str(n%3) + res
        n //= 3
    return res

def f(n):
    r = tr(n)
    if n % 3 == 0:
        r = r + r[-2:]
    else:
        z = tr(sum([int(x) for x in tr(n)]))
        r = r + z
    return int(r, 3)

for n in range(1, 100):
    if f(n) > 220 and f(n) % 2 == 0:
        print(f(n))
        break