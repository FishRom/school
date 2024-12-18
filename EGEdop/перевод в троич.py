def f1(n):
    r = ''
    while n > 0:
        r = str(n % 3) + r
        n //= 3
    return r