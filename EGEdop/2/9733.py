for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                a = (x and (not y)) or (x == z) or w
                if not a:
                    print(y, x, w, z)