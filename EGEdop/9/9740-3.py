with open('9_9740.csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        b = [x for x in a if a.count(x) == 3]
        c = [x for x in a if a.count(x) == 1]
        if len(b) == 3 and len(c) == 4 and sum(c)/4 <= b[0]:
            r += 1
print(r)