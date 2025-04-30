with open('9.csv', 'r') as f:
    r = 0
    for i in f:
        r += 1
        a = [int(x) for x in i.split(';')]
        z = 1
        for i in range(1, len(a)):
            if a[i - 1] >= a[i]:
                z = 0
                break
        if z == 0:
            continue
        if (a[0] + a[6])/2 < sum(a[1:6])/5:
            print(r)
            print(a)