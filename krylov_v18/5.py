def f(n):
    n = n - (n%4)
    r = bin(n)[2:]
    r = r + str((r.count('1') % 2))
    r = r + str((r.count('1') % 2))
    return int(r, 2)

for x in range(1, 1000):
    if f(x) > 100:
        print(f(x))
        break