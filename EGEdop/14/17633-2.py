def f(n):
    res = ''
    while n > 0:
        res = str(n%6) + res
        n //= 6
    return res

for x in range(1, 2031):
    n = (6**260+6**160+6**60-x)
    if f(n).count('0') == 202:
        print(x)
        break
