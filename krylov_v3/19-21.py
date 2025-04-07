def f(n, st, mst):
    if st > mst:
        return False
    if n <= 21:
        return st % 2 == mst % 2

    #new move

    st += 1
    a = []
    a.append(f(n-3, st, mst))
    a.append(f(n-7, st, mst))
    a.append(f(n//4, st, mst))

    if st % 2 == mst % 2:
        return any(a)
    else:
        return all(a)

for n in range(300, 21, -1):
    for mst in range(1, 5):
        if f(n, 0, mst):
            if mst == 4:
                print(n, mst)
            break