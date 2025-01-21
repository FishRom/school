def f(a):
    for x in range(0, 1000):
        for y in range(0, 1000):
            z = (x + 2*y > a) or (y < x) or (x < 30)
            if not z:
                return False
    return True

for a in range(0, 100):
    if f(a):
        print(a)
