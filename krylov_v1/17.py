with open('17var01.txt', 'r') as f:
    a = [int(x) for x in f]
    b = min([x for x in a])

    c =[]
    for i in range(0, len(a) - 1):
        if [x for x in a[i:i+2] if x % 27 == b]:
            c.append(sum(a[i:i+2]))
print(len(c), max(c))