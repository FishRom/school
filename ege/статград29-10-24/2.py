for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                a = (x <= (y <= z)) and (y <= (z == (not(w))))
                if not a:
                    print(w, z, y, x)