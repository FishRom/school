with open('09_9778(1).csv', 'r') as f:
    for z, i in enumerate(f):
        a = [int(x) for x in i.split(';')]
        b = [x for x in a if a.count(x) == 2]
        c = [x for x in a if a.count(x) == 1]
        if len(b) == 2 and len(c) == 4 and b[0] >= (sum(c)/4):
            print(a, b, c, z + 1)
            break
