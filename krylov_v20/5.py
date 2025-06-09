def f(n):
    n = n - (n%4)
    r = bin(n)[2:]
    r = r + str(r.count('1') % 2)
    r = r + str(r.count('1') % 2)
    return int(r, 2)

for n in range(1, 200):
    if f(n) < 47:
        print(n)