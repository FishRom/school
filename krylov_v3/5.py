def f(n):
    r = bin(n)[2:]
    if n % 4 == 0:
        r = r + r
    else:
        r = r + r[::-1]
    return int(r, 2)


a = []
for n in range(100):
    if f(n) >= 544:
        a.append(n)
print(min(a))