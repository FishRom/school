def f(k):
    n = '8' + '4' * k
    while '11' in n or '444' in n or '8888' in n:
        if '11' in n:
            n = n.replace('11', '4', 1)
        if '444' in n:
            n = n.replace('444', '88', 1)
        if '8888' in n:
            n = n.replace('8888', '1', 1)
    return n

a = []
for n in range(3, 10001):
    z = sum([int(x) for x in f(n)])
    a.append(z)
print(max(a))