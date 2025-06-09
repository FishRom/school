def f(a):
    for x in range(1000):
        for y in range(1000):
            z = (4*x + y < a) or (x < y) or (22 <= x)
            if z == 0:
                return False
    return True

for a in range(1000):
    if f(a):
        print(a)
        break