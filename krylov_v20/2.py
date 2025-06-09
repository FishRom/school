for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                a = (z <= x) and (not(w)) and y
                if a:
                    print(w, z, y, x)