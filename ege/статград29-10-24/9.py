with open('Копия 09.csv', 'r') as f:
    r = 1
    for i in f:
        a = [int(x) for x in i.split(';')]
        b = [x for x in a if a.count(x) >= 3]
        c = [x for x in a if a.count(x) == 1]
        #a.sort()
        #if len(b) >= 3 and len(c) > 0:
        #    print(a, b, c)
        if (len(b) >= 3) and (len(c) >= 1) and (sum(b)/len(b) > sum(c)/len(c)):
            r += 1
print(r)
#32

