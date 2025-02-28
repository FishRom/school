with open('17_9786.txt', 'r') as f:
    a = [int(x) for x in f]
    z = max([x for x in a if x % 100 == 25])
    #print(z)

    b = []
    for i in range(0, len(a) - 2):
        z1 = len([x for x in a[i:i+3] if len(str(abs(x))) == 4])
        if sum(a[i:i+3]) <= z and z1 <= 2:
            #print(z1)
            b.append(sum(a[i:i+3]))
print(len(b), max(b))