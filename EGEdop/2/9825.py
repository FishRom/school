for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                a = (x <= (z == w)) or (not(y <= w))
                if not a:
                    print(z, w, y, x)