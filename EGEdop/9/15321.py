with open('9_15321.csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        a.sort()
        #print(a)
        if a[3] < sum(a[0:3]) and (a[0] + a[3] == a[1] + a[2]):
            r += 1
print(r)