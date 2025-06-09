with open('9var6.csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        print(a)
        b = [x for x in a if a.count(x) == 2]
        c = [x for x in a if a.count(x) == 1]

        if len(b) == 6 and len(c) == 2 and min(a) in c:
            r += 1
print(r)