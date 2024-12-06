with open('9_26.csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        a.sort()
        b = [x for x in a if a.count(x) == 2]
        c = [x for x in a if a.count(x) == 1]
        if len(b) >= 2 and len(c) <= 5 and sum(c) % 2 != 0:
            r += 1
print(r)