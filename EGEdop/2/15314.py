for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                a = (x and (not(z))) or (y == z) or (not w)
                if not a:
                    print(w, y, z, x)