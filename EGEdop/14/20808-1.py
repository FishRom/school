def f(n):
    res = ''
    while n > 0:
        res = str(n%7) + res
        n //= 7
    return res

a = []
for x in range(1, 2030):
    a.append((f(7**710 + 7**100 - x).count('0'), x))
a.sort()
print(a[-10:])
