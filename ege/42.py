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
for i in range(2496, 7084):
    f = convert(i, 16)
    if (f[-2:] == '1A' or f[-2:] == '1F') and (i % 5 != 0) and (i % 9 != 0):
        c.append(i)
k = len(c)
maxi = min(c)
print(k, maxi)