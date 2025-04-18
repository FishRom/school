with open('17_21416.txt', 'r') as f:
    a = [int(x) for x in f]
    ot = [x for x in a if x < 0]

    b = []
    for i in range(0, len(a) - 2):
        if max(a[i:i+3]) * min(a[i:i+3]) > sum(ot):
            b.append(sum(a[i:i+3]))
print(len(b), max(b))