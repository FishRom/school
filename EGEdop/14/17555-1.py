def f(n, x):
    res = ''
    while n > 0:
        res = str(n%x) + res
        n //= x
    return res

for i in range(1, 2031):
    if f(7**91 + 7**160 - i, 7).count('0') == 70:
        print(i)