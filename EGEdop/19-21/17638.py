def f(s1, p, mst):
    if p > mst:
        return False
    if s1 >= 39:
        return p % 2 == mst % 2

    #new move

    p += 1
    a = []

    a.append(f(s1 + 1, p, mst))
    a.append(f(s1 + 3, p, mst))
    a.append(f(s1 * 2, p, mst))

    if p % 2 == mst % 2:
        return any(a)
    else:
        return all(a)

for s in range(1, 39):
    for mst in range(1, 5):
        if f(s, 0, mst):
            if mst == 3:
                print(s, mst)
            break