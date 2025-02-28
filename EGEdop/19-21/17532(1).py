def f(n1, n2, st, mst):
    if st > mst:
        return False
    if n1 + n2 >= 65:
        return st % 2 == mst % 2

    #new move

    st += 1
    a = []
    a.append(f(n1 + 1, n2, st, mst))
    a.append(f(n1 * 3, n2, st, mst))
    a.append(f(n1, n2 + 1, st, mst))
    a.append(f(n1, n2 * 3, st, mst))

    if st % 2 == mst % 2:
        return any(a)
    else:
        return all(a)

for n2 in range(1, 59):
    for mst in range(1, 5):
        if f(6, n2, 0, mst):
            if mst == 4:
                print(n2, mst)
            break