def f(k):
    n = '1' + '2'*k
    while '12' in n or '5522' in n or '2222' in n:
        if '12' in n:
            n = n.replace('12', '55', 1)
        if '2222' in n:
            n = n.replace('2222', '1', 1)
        if '5522' in n:
            n = n.replace('5522', '21', 1)
    return n

for n in range(4, 10000):
    z = sum([int(x) for x in f(n)])
    if z == 142:
        print(n)
        break