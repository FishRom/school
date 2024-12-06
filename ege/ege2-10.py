for x in range(2):
    for y in range(2):
        for z in range(2):
            #1a = not(x) or y or not(z)
            a = not(x) and y and z
            #a = x and not(y) and not(z)
            ##a = not(x) or not(y) and z
            if a:
                print(x, y, z)