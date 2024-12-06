#задача номер 3
with open('Копия 9_3.csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        #b = [x for x in a if 90 in a]
        a.sort()
        if sum(a) == 180 and a[2] == 90 and a[0] > 0:
            r += 1
print(r)

#109