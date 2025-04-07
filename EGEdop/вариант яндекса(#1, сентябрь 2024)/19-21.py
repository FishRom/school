def f1(n1, n2, st, mst):
    if st > mst:
        return False
    if n1+n2 >= 181:
        return st % 2 == mst % 2

    #new move

    st += 1
    a = []
    a.append(f1(n1 + 4, n2, st, mst))
    a.append(f1(n1, n2 + 4, st, mst))
    a.append(f1(n1 * 3, n2, st, mst))
    a.append(f1(n1, n2 * 3, st, mst))

    if st % 2 == mst % 2:
        return any(a)
    else:
        return all(a)

for n2 in range(1, 156):
    for mst in range(1, 5):
        if f1(25, n2, 0, mst):
            if mst == 3:
                print(n2, mst)