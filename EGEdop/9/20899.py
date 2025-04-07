with open('9_20899.csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        a.sort()
        b = [x for x in a if a.count(x) == 2]
        if a[3] < (a[0] + a[1] + a[2]) and len(b) == 2:
            r += 1
print(r)