with open('17_12249.txt', 'r') as f:
    a = [int(x) for x in f]
    #print(a[:20])
    z = max([x for x in a if x % 10 == 3])

    b = []
    for i in range(0, len(a) - 2):
        print(a[i:i + 3])
        if len([x for x in a[i:i+3] if abs(x) % 10 == 3]) > 0 and sum(a[i:i+3]) <= z:
            b.append(sum(a[i:i+3]))
    print(len(b), max(b))

    #print(a[-10:])