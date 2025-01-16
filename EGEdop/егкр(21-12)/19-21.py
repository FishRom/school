def f(n1, st, mst):
    if st > mst:
        return False
    if n1 >= 132:
        return st % 2 == mst % 2

    #new move

    st += 1
    a = []
    a.append(f(n1 + 3, st, mst))
    a.append(f(n1 + 6, st, mst))
    a.append(f(n1 * 3, st, mst))

    if st % 2 == mst % 2:
        return any(a)
    else:
        return all(a)

for n in range(1, 132):
    for mst in range(1, 5):
        if f(n, 0, mst):
            if mst == 4:
                print(n, mst)
            break