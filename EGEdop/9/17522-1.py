with open('9_17522.csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        a.sort()
        b = [x for x in a if a.count(x) == 2]
        #print(a)
        if len(b) == 2 and a[3] < sum(a[0:3]):
            r += 1
print(r)