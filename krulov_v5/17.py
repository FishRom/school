with open('17var05.txt', 'r') as f:
    a = [int(x) for x in f]
    m = min([x for x in a if x % 100 == 25])

    b = []
    for i in range(0, len(a) - 2):
        if len([x for x in a[i:i+3] if len(str(x)) == 2]) == 1 and sum(a[i:i+3]) < m:
            b.append(sum(a[i:i+3]))
print(len(b), max(b))