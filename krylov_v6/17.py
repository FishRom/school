with open('17var06.txt', 'r') as f:
    a = [int(x) for x in f]
    m = max([x for x in a if x % 1000 == 100])

    v = []
    for i in range(0, len(a) - 2):
        if len([x for x in a[i:i+3] if len(str(x)) == 3]) == 2 and sum(a[i:i+3]) <= m:
            v.append(sum(a[i:i+3]))
print(len(v), max(v))