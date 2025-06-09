def f(k):
    n = '>' + '1' * 11 + '2' * k + '3' * 11
    while '>1' in n or '>2' in n or '>3' in n:
        if '>1' in n:
            n = n.replace('>1', '222>', 1)
        if '>2' in n:
            n = n.replace('>2', '3>', 1)
        if '>3' in n:
            n = n.replace('>3', '1>', 1)
    return n.replace('>', '')


def p(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for n in range(1, 200):

    z = sum([int(x) for x in f(n)])
    if p(z):
        print(n)
