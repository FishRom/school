'''import math

def f1(y):
    if y > 6:
        return 0
    else:
        return 1

with open('27_A_19257.txt', 'r') as f:
    f.readline()
    lenn = 2
    a =[[] for x in range(lenn)]
    for i in f:
        x,y = map(float, i.replace(',', '.').split())
        a[f1(y)].append([x,y])

    b = [[] for x in range(lenn)]
    for ind, val in enumerate(a):
        z = 10.0**10
        for q in val:
            zz = sum(math.hypot(q[0] - x[0], q[1] - x[1]) for x in val)
            if z > zz:
                z = zz
                b[ind] = q
    print(b)
    px = int((sum(x[0] for x in b) / lenn) * 10000)
    py = int((sum(x[1] for x in b) / lenn) * 10000)

print(px, py)
'''


def f(s1, p, mst):
    if p > mst:
        return False
    if s1 >= 132:
        return p % 2 == mst % 2

    #new move
    p += 1
    a = []
    a.append(f(s1 + 3, p, mst))
    a.append(f(s1 + 6, p, mst))
    a.append(f(s1 * 3, p, mst))


    if p % 2 == mst % 2:
        return any(a)
    else:
        return all(a)


for s in range(1, 132):
    for mst in range(1, 5):
        if f(s, 0, mst):
            if mst == 2:
                print(s, mst)
            break