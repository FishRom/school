def f(n, x):
    res = ''
    while n > 0:
        res = str(n%x) + res
        n //= x
    return res

for x in range(1, 2031):
    if f(3**100 - x, 3).count('0') == 5:
        print(x)