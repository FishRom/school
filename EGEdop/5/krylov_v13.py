def f(n):
    r = str(n)
    a = []
    a.append(sum([int(x)**2 for x in r[:-1]]))
    a.append(sum([int(x)**2 for x in r[1:]]))
    a.sort()
    return int(str(a[1]) + str(a[0]))
#print(f(621))

a = []
for n in range(100, 1000):
    if f(n) == 9752:
        print(n)

