with open('17var11.txt', 'r') as f:
    a = [int(x) for x in f]
    m = max([x for x in a])

    v = []
    for i in range(0, len(a) - 2):
        if len([x for x in a[i:i+3] if x % 10 == 0]) == 1 and sum(a[i:i+3]) < m:
            v.append(sum(a[i:i+3]))
print(len(v), max(v))