def f(n):
    r = ''
    while n > 0:
        r = str(n % 6) + r
        n //= 6
    return r

z = 6**260 + 6**160 + 6**60
for x in range(2030):
    if f(z - x).count('0') == 202:
        print(x)
        break