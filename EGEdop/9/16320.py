with open('9_16320.csv', 'r') as f:
    res = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        a.sort()
        if a[3] < sum(a[:3]) and a[0] + a[3] == a[2] + a[1]:
            res += 1
print(res)