with open('9-161 (1).csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        a.sort()
        print(a)
        b = [x for x in a if a.count(x) == 2]
        c = [x for x in a if a.count(x) == 1]
        if a[3] < (a[0] + a[1] + a[2]) and (len(b) == 2 and len(c) == 2):
            r += 1
print(r)