with open('17_17873.txt', 'r') as f:
    a = [int(x) for x in f]
    m = min(a)
    b = []
    for i in range(0, len(a) - 1):
        if len([x for x in a[i:i+2] if x % 16 == m]) > 0:
            b.append(sum(a[i:i+2]))
print(len(b), max(b))
