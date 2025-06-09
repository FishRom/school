def f(k):
    n = '1' + '2'* k
    while '12' in n or '3322' in n or '2222' in n:
        if '12' in n:
            n = n.replace('12', '33', 1)
        if '2222' in n:
            n = n.replace('2222', '1', 1)
        if '3322' in n:
            n = n.replace('3322', '21', 1)
    return n

for n in range(3, 10000):
    z = sum([int(x) for x in f(n)])
    if z == 218:
        print(n)
        break
