with open('09_9778.csv', 'r') as f:
    r = 1
    for i in f:
        a = [int(x) for x in i.split(';')]
        #print(a)
        b = [x for x in a if a.count(x) == 2]
        c = [x for x in a if a.count(x) == 1]
        if (len(b) == 2) and (len(c) == 4) and (b[0] >= sum(c)/4):
            print(r)
            break
        r += 1