with open('9_18.csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        a.sort()
        print(a)
        '''b = [x for x in a if x % 10 == 3]
        c = [x for x in a if x > 0]
        d = [x for x in a if x < 0]
        if (len(b) == 3) and ((sum(c)**2) < sum(d)**2):
            r += 1
print(r)'''