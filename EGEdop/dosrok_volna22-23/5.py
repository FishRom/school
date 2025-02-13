def f(n):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r + r[-3:]
    else:
        r = r + bin((n%3)*3)[2:]
    return int(r, 2)

a = []
for i in range(1, 500):
    if f(i) < 100:
        a.append(i)
print(max(a))