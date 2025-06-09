for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                a = (z <= w) and y and (not(x))
                if (a == 0 and x + y + z + w >= 2) or (a == 1 and x + z + y + w <= 3) or (a == 1 and x + z + y + w <= 2):
                    print(z, w, y, x, a)