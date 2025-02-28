with open('9_12241.csv', 'r') as f:
    res = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        b = [x for x in a if a.count(x) == 2]
        c = [x for x in a if a.count(x) == 1]
        b.sort()

        if (len(b) == 6 and len(c) == 1) and ((b[0] + b[-1])/2) < c[0]:
            res += 1
print(res)