#1
'''for x in range(2):
    for y in range(2):
        for w in range(2):
            a = not(x) and (not(y) or w)
            if a:
                print(x, w, y)'''

#2
'''for x in range(2):
    for y in range(2):
        for z in range(2):
            a = (x and not(z)) or (x and y and z)
            if a:
                print(y, z, x)'''

#3
'''for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                a = (x or not(y)) and not(y == z) and not(w)
                if a:
                    print(x, z, y, w)'''

#4
'''
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                a = x <= (y and not(w) or z)
                if not a:
                    print(y, w, z, x)'''

#5
'''for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                a = ((not x) <= y) and ((not y) == z) and w
                if a:
                    print(x, z, y, w)'''

#6

'''for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                a = not(x and (y or z) and (z or w) and (y or not(w)))
                if not a:
                    print(x, z, y, w)'''

#7
'''for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                a = ((y <= w) == (x <= (not z))) and (x or w)
                print(y, x, w, z, a)'''
