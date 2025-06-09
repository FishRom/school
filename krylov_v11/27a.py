import math


def f1(y):
    if y > 15:
        return 0
    else:
        return 1

with open('27var11A.txt', 'r') as f:
    f.readline()
    lenn = 2
    a = [[] for x in range(lenn)]
    for i in f:
        x, y = map(float, i.replace(',', '.').split())
        a[f1(y)].append([x, y])
    b = [[] for x in range(lenn)]

    for ind, val in enumerate(a):
        z = 10.0**10
        for q in val:
            tr = sum(math.hypot(q[0] - x[0], q[1] - x[1]) for x in val)
            if z > tr:
                z = tr
                b[ind] = q
    px = int((sum(x[0] for x in b) / lenn) * 10000)
    py = int((sum(x[1] for x in b) / lenn) * 10000)
print(px, py)