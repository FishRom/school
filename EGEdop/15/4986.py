for a in range(1, 100):
    res = 1
    for x in range(1, 1000):
        z = (x % a == 0) or ((x % 23 == 0) <= (not(50 <= x <= 70)))
        if z == 0:
            res = 0
            break
    if res == 1:
        print(a)