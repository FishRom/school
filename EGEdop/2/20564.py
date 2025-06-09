for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                a = x and ((w <= y) == z)
                if (a == 0 and x + y + z + w >= 3) or (a == 1 and x + y + w + z <= 2):
                    print(z, x, w, y, a)