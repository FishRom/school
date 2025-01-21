def f(k):
    n = '3' + '5' * k
    while '25' in n or '355' in n or '555' in n:
        if '25' in n:
            n = n.replace('25', '32', 1)
        if '355' in n:
            n = n.replace('355', '25', 1)
        if '555' in n:
            n = n.replace('555', '3', 1)
    return n

a = []
for n in range(3, 10001):
    z = sum([int(x) for x in f(n)])
    if z == 17:
        print(n)
        break