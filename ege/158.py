for x in range(2):
    for y in range(2):
        for z in range(2):
            a = not(x) and y and z
            if a:
                print(x, y, z)