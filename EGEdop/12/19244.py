def f(k):
    n = '1' + '2' * k
    while '12' in n or '322' in n or '222' in n:
        if '12' in n:
            n = n.replace('12', '2', 1)
        if '322' in n:
            n = n.replace('322', '21', 1)
        if '222' in n:
            n = n.replace('222', '3', 1)
    return n

for i in range(3, 10_000):
    z = sum([int(x) for x in f(i)])
    if z == 15:
        print(i)
        break