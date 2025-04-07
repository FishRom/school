with open('17.txt', 'r') as f:
    a = [int(x) for x in f]
    z = min([x for x in a if x % 2025 == 0])

    v = []
    for i in range(0, len(a) - 2):
        if len([x for x in a[i:i+3] if abs(x) % z == 0]) >= 1 and len(str(sum([x for x in a[i:i+3]]))) == 6:
            v.append(sum(a[i:i+3]))
print(len(v), max(v))