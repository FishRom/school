with open('9_16375.csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        b = [x for x in a if a.count(x) == 2]
        c = [x for x in a if a.count(x) == 1]
        c.sort()
        if len(b) == 2 and len(c) == 5 and c[0]*c[1]*c[2] > b[0]**2:
            r += 1
print(r)