with open('9_19241.csv', 'r') as f:
    q = 1
    for i in f:
        a = [int(x) for x in i.split(';')]

        b = [x for x in a if a.count(x) == 3]
        c = [x for x in a if a.count(x) == 1]
        if (len(b) == 6 and len(c) == 1) and (sum(b)/6 < c[0]):
            print(q)
        q +=1