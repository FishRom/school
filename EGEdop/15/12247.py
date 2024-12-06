for a in range(0, 100):
    res = 1
    for x in range(0, 1000):
        z = ((x&a == 0) or (x&37 != 0) or (x&12 != 0))
        if z == 0:
            res = 0
            break
    if res == 1:
        print(a)
