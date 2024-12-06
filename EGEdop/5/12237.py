def f(n):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + r[-2:]
    else:
        r = '1' + r + '0'
    return int(r, 2)
#print(f(10))
a = []
for n in range(1, 100):
    if f(n) < 100:
        a.append(n)
print(max(a))