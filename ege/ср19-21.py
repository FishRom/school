'''def f(s1, s2, p, mst):
    if p > mst:
        return False
    if s1 >= 479 or s2 >= 479:
        return p % 2 == mst % 2

    #new move
    p += 1
    a = []
    a.append(f(s1 + 1, s2, p, mst))
    a.append(f(s1 + 3, s2, p, mst))
    a.append(f(s1 * 2, s2, p, mst))
    a.append(f(s1, s2 + 1, p, mst))
    a.append(f(s1, s2 + 3, p, mst))
    a.append(f(s1, s2 * 2, p, mst))


    if p % 2 == mst % 2:
        return any(a)
    else:
        return all(a)


for s in range(1, 479):
    for mst in range(1, 5):
        if f(239, s, 0, mst):
            if mst == 4:
                print(s, mst)
            break'''

'''def f(s1, p, mst):
    if p > mst:
        return False
    if s1 >= 40:
        return p % 2 == mst % 2

    #new move

    p += 1
    a = []

    a.append(f(s1 + 2, p, mst))
    a.append(f(s1 * 2, p, mst))

    if p % 2 == mst % 2:
        return any(a)
    else:
        return all(a)

for s in range(1, 39):
    for mst in range(1, 5):
        if f(s, 0, mst):
            print(s, mst)
            break'''

def f(s1, s2, p, mst):
    if p > mst:
        return False
    if s1+s2 >= 67:
        return p % 2 == mst % 2

    #new move
    p += 1
    a = []
    a.append(f(s1 + s2, s2, p, mst))
    a.append(f(s1, s2 + s1, p, mst))

    if p % 2 == mst % 2:
        return any(a)
    else:
        return all(a)


for s in range(1, 55):
    for mst in range(1, 5):
        if f(12, s, 0, mst):
            if mst == 4:
                print(s, mst)
            break