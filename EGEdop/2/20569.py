for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                a = (((w <= z) == (x <= (not y))) and (x or z))
                if  (a == 0 and x + y + w + z == 3) or(x + y + z + w <= 2 and a == 1):
                    print(z, x, y, w, a)