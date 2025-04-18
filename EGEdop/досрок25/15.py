def f(a):
    for x in range(1000):
        for y in range(1000):
            z = (5 < y) or (x > 32) or (x + 2*y < a)
            if not z:
                return 0
    return 1

for a in range(2, 100):
    if f(a):
        print(a)
        break

