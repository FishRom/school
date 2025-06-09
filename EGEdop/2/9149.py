for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                a = ((x <= y) or (z == x)) and (w <= z)
                if (a == 1 and x + y + z + w == 2) or (a == 0 and x + y + z + w == 3) or (a == 0 and x + y + z + w == 1):
                    print(z, w, x, y, a)