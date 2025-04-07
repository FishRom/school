for a in range(1, 500):
    r = 1
    for x in range(1, 500):
        z = ((x % 14 == 0) <= (not(x % 4 == 0))) or (x + a >= 200)
        if z == 0:
            r = 0
            break
    if r == 1:
        print(a)