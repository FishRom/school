
for a in range(1, 100):
    res = 1
    for x in range(1, 2000):
        z = ((x % 3 == 0) <= (x % 5 != 0)) or (x + a >= 70)
        if z == 0:
            res = 0
            break
    if res == 1:
        print(a)
        break