def f(n):
    r = ''
    while n > 0:
        r = str(n%9) + r
        n //= 9
    return r

for x in range(0, 5769+1):
    if f(9**2025 + 9**1000 - x).count('0') == 1026:
        print(x)
        break