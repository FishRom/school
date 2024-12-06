def f1(n):
    r = ''
    while n > 0:
        r = str(n % 3) + r
        n //= 3
    return r
#print(f1(3))

def f(n):
    r = f1(n)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r = r + f1(4 * (n % 3))
    return int(r, 3)


a = []
for n in range(1, 200):
    if f(n) < 199:
        a.append(n)
print(max(a))


