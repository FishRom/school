def f(k):
    n = '3' + '5' * k
    while '25' in n or '355' in n or '555' in n:
        if '25' in n:
            n = n.replace('25', '3', 1)
        if '355' in n:
            n = n.replace('355', '52', 1)
        if '555' in n:
            n = n.replace('555', '23', 1)
    return n

for n in range(4, 100):
    z = sum([int(x) for x in f(n)])
    if z == 27:
        print(n)