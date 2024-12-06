def f(n):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r + r[-3:]
    else:
        r = r + bin(3 * (n % 3))[2:]
    return int(r, 2)

a = []
for n in range(1, 170):
    if f(n) < 170:
        a.append(f(n))
print(max(a))