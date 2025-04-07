with open('9var3.csv', 'r') as f:
    res = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        a.sort()
        b = [x for x in a if a.count(x) == 2]
        c = [x for x in a if a.count(x) == 1]
        z = [x for x in a if x != a[0] and x != a[3] and x > 23]
        if len(b) == 2 and len(z) > 0:
            res += 1
    print(res)