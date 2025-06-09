with open('Копия 325_9.csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        b = [x for x in a if a.count(x) == 2]
        c = [x for x in a if a.count(x) == 1]

        if len(b) == 4 and len(c) == 3 and max(b) < max(c):
            r += 1
print(r)