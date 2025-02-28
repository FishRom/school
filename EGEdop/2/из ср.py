for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f1 = (w==x) and (y<=z)
                f2 = (w<=x) <= (y==z)
                if f1 == 1 and f2 == 0 and x+y+w+z >= 3:
                    print(x,y,w,z, 'первое условие')
                if f1 == 0 and f2 == 0 and x+y+w+z <= 2:
                    print(x,y,w,z, 'second')
                if f1 == 1 and y == 1 and w == 0 and x+y+z+w <= 2:
                    print(z,y,w,x, 'three')
