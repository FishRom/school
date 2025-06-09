for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                a = (not(y <= (not(z <= w)))) and ( (not(z)) <= ((not(w)) == x) )
                if a:
                    print(y, w, z, x)