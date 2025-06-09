with open('9var9-12.csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        a.sort()
        if a[1]-a[0] == a[3]-a[2] == a[2]-a[1] or a[3]**2 > a[0]*a[1]*a[2]:
            print(a)
            r += 1
print(r)