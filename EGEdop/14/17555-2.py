def f(n):
    res = ''
    while n > 0:
        res = str(n%7) + res
        n //= 7
    return res

for x in range(1, 2031):
    n = 7**91+7**160-x
    if f(n).count('0') == 70:
        print(x)