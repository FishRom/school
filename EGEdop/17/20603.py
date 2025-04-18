with open('17_20603_20603.txt', 'r') as f:
    a = [int(x) for x in f]
    m = max([x for x in a if x % 10 == 5])

    b = []
    for i in range(0, len(a) - 2):
        if len([x for x in a[i:i+3] if len(str(x)) == 5]) == 2 and sum(a[i:i+3]) > m:
            b.append(sum(a[i:i+3]))
print(len(b), max(b))