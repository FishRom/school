def f(n):
    r = ''
    while n > 0:
        r = str(n % 7) + r
        n //= 7
    return r

z = 7 ** 91 + 7 ** 160
for x in range(2030, 1, -1):
    if f(z - x).count('0') == 70:
        print(x)
        break