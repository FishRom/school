for a in range(1, 1000):
    r = 1
    for x in range(1, 1000):
        z = (x % a == 0) or ((200 <= x <= 300) <= (not(x % 77 == 0)))
        if z == 0:
            r = 0
            break
    if r == 1:
        print(a)