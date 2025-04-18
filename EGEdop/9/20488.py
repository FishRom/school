with open('9.22_20488.csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        a.sort()
        b = [x for x in a if a.count(x) == 1]