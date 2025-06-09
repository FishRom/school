with open('17var12.txt', 'r') as f:
    a = [int(x) for x in f]
    m = max([x for x in a])

    v = []
    h = []
    for i in range(0, len(a) - 2):
        if len([x for x in a[i:i+3] if x % 10 == 3]) == 0 and (a[i]**2 + a[i+1]**2 + a[i+2]**2) > m:
            v.append(sum(a[i:i+3]))
            g = a[i]**2 + a[i+1]**2 + a[i+2]**2
            h.append(g)
print(len(v), min(h))