def f(n):
    r = bin(n)[2:]
    if len(r) % 2 == 0:
        r = r[:len(r)//2] + '1' + r[len(r)//2:]
    else:
        r = r
    return int(r, 2)

for n in range(100):
    if f(n) > 26:
        print(n)
        break