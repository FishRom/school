def f(n1, st, mst):
    if st > mst:
        return False
    if n1 >= 78:
        return st % 2 == mst % 2

    #new move

    st += 1
    a = []
    a.append(f(n1 + 1, st, mst))
    a.append(f(n1 + 4, st, mst))
    a.append(f(n1 * 4, st, mst))
    if st % 2 == mst % 2:
        return any(a)
    else:
        return all(a)

for s in range(1, 78):
    for mst in range(1, 5):
        if f(s, 0, mst):
            if mst == 4:
                print(s, mst)