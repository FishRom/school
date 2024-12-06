for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                a = (not (x or y)) and (not w) or (not (z or w)) and y
                if a:
                    print(w, y, z, x)