import math

def f1(x, y):
    if y > 5.2 and x > 1:
        return 0
    elif (x > 2 and x < 6.8 and y > 2) or (6.8 < x < 10 and y > 0):
        return 1
    elif (x < 2 and y < 5.2) or (2 < x < 6.8 and y < 2):
        return 2
    else:
        return 3


with open('27-38b.txt', 'r') as f:
    f.readline()
    lenn = 3
    a = [[] for x in range(lenn)]
    for i in f:
        x,y = map(float, i.replace(',', '.').split())
        w = f1(x, y)
        if w < 3:
            a[w].append([x, y])

    b = [[] for x in range(lenn)]

    for ind, val in enumerate(a):
        z = 10.0**10
        for q in val:
            zz = sum([math.hypot(q[0] - x[0], q[1] - x[1]) for x in val])
            if z > zz:
                b[ind] = q
                z = zz

    px = int((sum([x[0] for x in b]) / lenn) * 100000)
    py = int((sum([x[1] for x in b]) / lenn) * 100000)
print(px, py)