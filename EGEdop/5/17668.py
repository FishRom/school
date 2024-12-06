def f(n):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '10' + r[2:] + '0'
    else:
        r = '11' + r[2:] + '1'
    print(n, r, int(r, 2))
    return int(r, 2)
print(f(38))
a = []
for n in range(1, 100):
    if n > 27:
     a.append(f(n))
print(min(a))


