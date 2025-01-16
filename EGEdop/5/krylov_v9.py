def f(n):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + '0'
    else:
        r = r + '1'

    if r.count('1') % 3 == 0:
        r = '11' + r[2:]
    else:
        r = '10' + r[2:]
    return int(r, 2)

#print(f(3))

a = []
for n in range(1, 26):
    if f(n) >= 26:
        print(n)
        break