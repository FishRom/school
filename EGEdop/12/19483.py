def f(k):
    n = '2' + '5'*k
    while '25' in n or '255' in n or '555' in n:
        if '25' in n:
            n = n.replace('25', '5', 1)
        if '355' in n:
            n = n.replace('355','522', 1)
        if '555' in n:
            n = n.replace('555', '3', 1)
    return n

for i in range(3, 10_000):
    if f(i).count('2') == 10:
        print(i)
        break