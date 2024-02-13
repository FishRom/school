def convert(n, base):
    if n == 0:
        return '0'
    stifri = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    while n > 0:
        digit = n % base
        res = stifri[digit] + res
        n //= base
    return res
c = []
for i in range(1000, 10000):
    f = convert(i, 6)
    if (f[-2:] == '13' or f[-2:] == '14') and len(f) <= 5:
        c.append(i)

print(len(c), max(c))