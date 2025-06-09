with open('9var9-12.csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        a.sort()
        if a[0]**2 > (a[1] + a[2] + a[3]) and a[0] % 2 != 0 and a[1] % 2 != 0 and a[2] % 2 != 0 and a[3] % 2 != 0:
            r += 1
print(r)