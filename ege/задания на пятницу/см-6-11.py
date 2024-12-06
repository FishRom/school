with open('9-170.csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        b = [x for x in a if a.count(x) == 2]
        c = [x for x in a if a.count(x) == 1]
        c.sort()
        print(c)
        if (len(b) == 2 and len(c) == 4) and max(c) + min(c) <= sum(b):
            r += 1
print(r)