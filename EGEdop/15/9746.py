for a in range(0, 100):
    res = 1
    for x in range(0, 1000):
        for y in range(0, 1000):
            z = ((x < a) or (y < a) or (x + 2*y > 50))
            if z == 0:
                res = 0
                break
        if res == 0:
            break
    if res == 1:
        print(a)
        break
