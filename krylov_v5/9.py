with open('9var5.csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        b = [x for x in a if a.count(x) == 3]
        c = [x for x in a if a.count(x) == 1]
        if len(b) == 6 and len(c) == 2 and max(c) > max(b):
            r += 1
print(r)