for a in range(0, 100):
    res = 1
    for x in range(0, 1000):
        for y in range(0, 1000):
            z = ((x*y < a) or (x < y) or (9 < x))
            if z == 0:
                res = 0
                break
        if res == 0:
            break
    if res == 1:
        print(a)
        break