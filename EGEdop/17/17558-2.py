with open('17_17558.txt', 'r') as f:
    a = [int(x) for x in f]
    kr = len([x for x in a if x % 32 == 0])

    b = []
    for i in range(0, len(a) - 1):
        if len([x for x in a[i:i+2] if x < 0]) > 0 and sum(a[i:i+2]) < kr:
            b.append(sum(a[i:i+2]))
print(len(b), max(b))