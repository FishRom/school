def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            z = (x**2 + y**2 > 128) or (y < -x + a)
            if not z:
                return False
    return True

for a in range(1, 1000):
    if f(a):
        print(a)
        break