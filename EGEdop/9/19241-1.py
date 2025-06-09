with open('9_19241.csv', 'r') as f:
    res = 0
    for i in f:
        res +=1
        a = [int(x) for x in i.split(';')]
        b = [x for x in a if a.count(x) == 3]
        c = [x for x in a if a.count(x) == 1]
        if len(b) == 6 and len(c) == 1 and sum(b)/6 < sum(c):
            print(res)
