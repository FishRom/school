for a in range(1, 200):
    res = 1
    for x in range(1, 1000):
        z = (x % a == 0) or ((50 <= x <= 70) <= (x % 16 != 0))
        if z == 0:
            #print(a, x)
            res = 0
            break
    if res == 1:
        print(a)
