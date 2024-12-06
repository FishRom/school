with open('9_12.csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        if (a[0] == 18 and a[1] == 18 and a[2] == 18 and a[3] == 18 and a[4] == 18) or sum(a) % 18 == 0:
            r += 1
print(r)
