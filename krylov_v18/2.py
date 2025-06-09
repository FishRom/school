for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                a = (not(z <= w)) or x or (not(y))
                if not a:
                    print(z, x, w, y)