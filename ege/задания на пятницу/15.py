with open('Копия 9_15.csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        a.sort()
        if (a[4] + a[0])/2 == a[1] or (a[4] + a[0])/2 == a[2] or (a[4] + a[0])/2 == a[3]:
            r += 1
print(r)




