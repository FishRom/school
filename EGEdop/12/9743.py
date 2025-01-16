
def f(k):
    n = '5' + '2' * k
    while '72' in n or '522' in n or '2222' in n:
        if '72' in n:
            n = n.replace('72', '2', 1)
        if '522' in n:
            n = n.replace('522', '27', 1)
        if '2222' in n:
            n = n.replace('2222', '5', 1)
    return n

for n in range(3, 10001):
    z = sum([int(x) for x in f(n)])
    if z == 63:
        print(n)
        break