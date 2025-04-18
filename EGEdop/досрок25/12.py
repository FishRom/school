def f(k):
    n = '3' + '1' * k
    while '31' in n or '211' in n or '1111' in n:
        if '31' in n:
            n = n.replace('31', '1', 1)
        if '211' in n:
            n = n.replace('211', '13', 1)
        if '1111' in n:
            n = n.replace('1111', '2', 1)
    return n

for i in range(3, 10_000):
    z = sum([int(x) for x in f(i)])
    if z == 15:
        print(i)
        break