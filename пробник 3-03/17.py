with open('17.txt', 'r') as f:
    a = [int(x) for x in f]
    b = max([x for x in a if x % 100 == 42])

    z = []
    for i in range(0, len(a) - 2):
        if len([x for x in a[i:i+3] if abs(x) % 100 == 42 and len(str(abs(x))) == 4]) >= 2 and a[i] + a[i+1] + a[i+2] > b:
            #z.append(sum(a[i:i+3]))
            z.append((a[i] + a[i+1] + a[i+2]))
    print(len(z), max(z))