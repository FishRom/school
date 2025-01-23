def f(a):
    for x in range(0, 1000):
        for y in range(0, 1000):
            z = ((x + y <= 24) or (y <= x - 2) or (y >= a))
            if not z:
                return False
    return True

for a in range(0, 100):
    if f(a):
        print(a)