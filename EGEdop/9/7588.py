with open('09_7588.csv', 'r') as f:
    res = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        b = [x for x in a if a.count(x) == 1]
        a.sort()
        print(a)
        if (len(b) == 5) and (3 * (a[0] + a[4]) <= 2 * sum(a[1:4])):
            res += 1
print(res)