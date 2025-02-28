with open('17_16383.txt', 'r') as f:
    a = [int(x) for x in f]
    b = max([x for x in a if x % 100 == 21])

    z = []
    for i in range(0, len(a) - 1):
        if len([x for x in a[i:i+2] if abs(x) % 100 == 21 and len(str(abs(x))) == 5]) == 1 and a[i]**2 + a[i+1]**2 >= b**2:
            z.append(sum(a[i:i+2]))
    print(len(z), max(z))