def f(n, x):
    res = ''
    while n > 0:
        res = str(n % x) + res
        n //= x
    return res

for x in range(1, 2031):
    if f(6**260+6**160+6**60-x, 6).count('0') == 202:
        print(x)
