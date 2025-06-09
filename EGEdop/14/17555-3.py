def f(n):
    res = ''
    while n > 0:
        res = str(n%7) + res
        n //= 7
    return res.count('0')

a = []
for x in range(1, 2031):
    if f(7**91 + 7**160 - x) == 70:
        print(x)