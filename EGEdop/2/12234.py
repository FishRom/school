for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                a = y and (x or z) or (not(y or z)) or w
                if not a:
                    print(x, y, w, z)