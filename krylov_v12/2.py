for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                a = (not(w <= (not(x <= y)))) and ( (not(x)) <= ( (not(y)) == z))
                if (a == 0 and x + y + z + w >= 3) or (a == 1 and x + y + z + w == 2):
                    print(y, w, z, x, a)