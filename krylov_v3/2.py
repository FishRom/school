for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                a = (not(x <= y)) or ((not(z)) == (w <= x)) or w
                if not a:
                    print(w, z, x, y)