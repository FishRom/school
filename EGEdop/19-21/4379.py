def f(n, st, mst, z):
    if st > mst:
        return False
    if n >= 51:
        return st % 2 == mst % 2



    #new move

    st += 1
    a = []
    if z == 0:
        if n * 2 < 60:
            z = 1
            a.append(f(n * 2, st, mst, z))
    else:
        if n + 1 < 60:
            a.append(f(n + 1, st, mst, z))
        if n + 2 < 60:
            a.append(f(n + 2, st, mst, z))
        if n * 2 < 60:
            a.append(f(n * 2, st, mst, z))

    if st % 2 == mst % 2:
        return any(a)
    else:
        return all(a)
for n in range(1, 51):
    for mst in range(1, 4):

        if f(n, 0, mst, 0):
            if mst == 3:
                print(n, mst)
            break