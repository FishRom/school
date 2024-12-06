with open('9_17522.csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        b = [x for x in a if a.count(x) == 2]
        c = [x for x in a if a.count(x) == 1]
        a.sort()
        if (a[3] < sum(a[0:3])) and (len(b) == 2) and (len(c) == 2):
            r += 1
print(r)
