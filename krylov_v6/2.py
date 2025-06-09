for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                a = (not(y <= x)) or (y == w) or z
                if not a:
                    print(z,y,w,x)