with open('9.15_20282.csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        a.sort()
        b = [x for x in a if a.count(x) == 3]
        if len(b) == 3 and (a[5]**2 + a[0]**2) >= (a[1] + a[2] + a[3] + a[4])**2:
            r += 1
print(r)