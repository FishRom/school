import math

def f1(x, y):
    if x > 7:
        return 0
    elif y > 1.5:
        return 1
    else:
        return 2

with open('27-4b.txt', 'r')as f:
    f.readline()
    lenn = 3
    a = [[] for x in range(lenn)]
    for i in f:
        x, y = map(float, i.replace(',', '.').split())
        a[f1(x, y)].append([x,y])

    b = [[] for x in range(lenn)]
    for ind, val in enumerate(a):
        z = 10.0**10
        for q in val:
            zz = sum(math.hypot(q[0] - x[0], q[1] - x[1]) for x in val)
            if z > zz:
                z = zz
                b[ind] = q

    px = int((sum(x[0] for x in b) / lenn) * 10000)
    py = int((sum(x[1] for x in b) / lenn) * 10000)
print(px, py)