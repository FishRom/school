with open('09_17550.csv', 'r') as f:
    res = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        b = [x for x in a if a.count(x) == 3]
        c = [x for x in a if a.count(x) == 1]
        if (len(b) == 3 and len(c) == 3) and (sum(b) > sum(c)):
            res += 1
print(res)