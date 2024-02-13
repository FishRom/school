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
    f = convert(i, 4)
    if i % 3 != 0 and i % 17 != 0 and i % 19 != 0 and len(f) == 6:
        c.append(i)
k = min(c)
maxi = max(c)
print(k, maxi)