for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                a = (not((((not(w)) <= (not(y))) <= (not(z))) <= x))
                if (a == 0 and x + y + z + w <= 1) or (a == 1 and x + y + w + z <= 2) or (a == 1 and x + y + w + z <= 1):
                    print(x, z, w, y, a)