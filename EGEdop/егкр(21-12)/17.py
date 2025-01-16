with open('17_19249.txt', 'r') as f:
    a = [int(x) for x in f]
    #print(a)
    m43 = max(x for x in a if x % 100 == 43)
    #print(m43)
    b = []
    for i in range(0, len(a) - 2):
        z = len([x for x in a[i:i+3] if len(str(abs(x))) == 5 and abs(x) % 100 == 43]) #т.к остатки разные, то у х надо писать abs()
        z1 = sum([x**2 for x in a[i:i+3]])
        if z >= 1 and z1 <= m43**2:
            b.append(z1)
print(len(b), min(b))


