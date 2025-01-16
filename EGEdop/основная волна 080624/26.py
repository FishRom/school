with open('26_17565.txt', 'r') as f:
    n, z = map(int, f.readline().split())
    a = []
    for i in f:
        t = [int(x) for x in i.split()]
        a.append((t[0], sum(t[1:4]), t[4]))
    a.sort(key=lambda x: (-x[1], -x[2],x[0]))
    print(a[z-1])
    print(a[z - 15:z + 15])
    print(len([x for x in a if x[1] == 154]))
    print(a)