def f(a):
    for x in range(1, 300):
        z = ((x & 52 != 0) and (x & 36 == 0)) <= (not(x & a == 0))
        if not z:
            return False
    return True

for a in range(1, 1000):
    if f(a):
        print(a)