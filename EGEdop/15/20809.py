for a in range(1, 100):
    r = 1
    for x in range(1, 100):
        z = (x % a == 0) or ((60 <= x <= 80) <= (not(x % 22 == 0)))
        if z == 0:
            r = 0
            break
    if r == 1:
        print(a)