with open('9var1.csv', 'r') as f:
    res = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        a.sort()
        print(a)
        c = [x for x in a if a.count(x) == 1]
        if len(c) == 4 and (a[3] < (a[0] + a[1] + a[2])):
            res += 1
print(res)