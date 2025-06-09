with open('9_21895.csv', 'r') as f:
    z = 0
    for i in f:
        a = [int(x) for x in i.split(';')]

        b = [x for x in a if a.count(x) == 1]


        b.sort()

        if len(b) == 5 and sum(b[3:]) <= sum(b[:3]):
            z += 1
            #print(b, len(b))
    print(z)