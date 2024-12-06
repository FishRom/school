def f(n):
    r = ''
    while n > 0:
        r = str(n % 3) + r
        n //= 3
    return r
z = 3**100
for x in range(2030, 1, -1):
    if f(z - x).count('0') == 5:
        print(x)
        break