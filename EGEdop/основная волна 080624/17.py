with open('17_17558.txt', 'r') as f:
    a = [int(x) for x in f]
    print(a[:20])
    b = len([x for x in a if x % 32 == 0])
    print(b)
    d = []
    for i in range(len(a) - 1):
        z = len([x for x in a[i:i + 2] if x < 0])
        if z > 0 and sum(a[i:i+2]) < b:
            d.append(sum(a[i:i+2]))
print(len(d), max(d))
