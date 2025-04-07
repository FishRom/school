def f(n):
    res = ''
    while n > 0:
        res = str(n % 5) + res
        n //= 5
    return res

for x in range(1, 100):
    if f(5**2025+5**1500-x).count('0') == 527:
        print(x)