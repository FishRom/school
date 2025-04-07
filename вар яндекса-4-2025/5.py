def f(n):
    r = bin(n)[2:]
    if n % 2 != 0:
        r = '1' + r.replace(r[-2:], '10')
    else:
        r = r.replace(r[:2], '10') + '1'

    return int(r, 2)

a = []
for n in range(33, 100):
    a.append(f(n))
print(min(a))