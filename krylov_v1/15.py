for a in range(1, 100):
    r = 1
    for x in range(1, 100):
        z = ((x % 9 == 0) <= (not(x % 6 == 0))) or (x + a >= 100)
        if z == 0:
            r = 0
            break
    if r == 1:
        print(a)