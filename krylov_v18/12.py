def f(k):
    n = '>' + '0' * 15 + '1' * k + '2' * 15
    while '>0' in n or '>1' in n or '>2' in n:
        if '>0' in n:
            n = n.replace('>0', '22>', 1)
        if '>1' in n:
            n = n.replace('>1', '2>', 1)
        if '>2' in n:
            n = n.replace('>2', '1>', 1)
    return n.replace('>', '')

def p(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for x in range(1, 100):
    z = sum([int(x) for x in f(x)])
    if p(z):
        print(x)