def f(n):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + r[-2:]
    else:
        r = r + r[-3:]

    return int(r, 2)
#print(f(1))

a = []
for n in range(1, 256):
    if f(n) > 256:
        print(n)
        break