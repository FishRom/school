def f(n):
    r = ''
    while n > 0:
        r = str(n % 6) + r
        n //= 6
    return r

for x in range(1000):
    if f(6**2025 + 6**25 - x).count('0') == 2002:
        print(x)