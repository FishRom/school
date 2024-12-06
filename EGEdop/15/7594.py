for a in range(0, 100):
    res = 1
    for x in range(0, 1000):
        z = (x&39 == 0) or ((x&11 == 0) <= (x&a != 0))
        if z == 0:
            res = 0
            break
    if res == 1:
        print(a)
        break