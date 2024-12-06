with open('Копия 9_13.csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        a.sort()
        if (a[0] + a[3]) % 3 == 0 and a[0] + a[3] == a[1] + a[2]:
            r += 1
print(r)




