#19
def f(n1,st,mst):
    if st > mst:
        return False
    if n1 >= 165:
        return st % 2 == mst % 2

    #новый ход
    st += 1
    a = []
    a.append(f(n1 + 1, st, mst))
    a.append(f(n1 + 4, st, mst))
    a.append(f(n1 * 2, st, mst))

    if st % 2 == mst % 2:
        return any(a)
    else:
        return all(a)

#далее перебор всевозможных вариантов
for n in range(1, 165):
    for mst in range(1, 5):
        if f(n, 0, mst):
            if mst == 4:
                print(n, mst)
            break