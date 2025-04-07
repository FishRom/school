def f(n):
    res = ''
    while n > 0:
        res = str(n%16) + res
        n //= 16
    return res

z = 16**560 + 16**120
for x in range(400):
    if f(z - x).count('0') == 442:
        print(x)
        break