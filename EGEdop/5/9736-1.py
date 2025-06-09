def f(n):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r + r[-3:]
    else:
        r = r + bin((n%3)*3)[2:]

    return int(r, 2)

a = []
for n in range(0, 100):
    if f(n) <= 170:
        a.append(f(n))
print(max(a))