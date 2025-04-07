for u in range(2):
    for x in range(2):
        for y in range(2):
            for w in range(2):
                v = (x <= w) <= (u <= y)
                if not v:
                    print(x, u, w, y)