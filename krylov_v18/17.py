with open('17var18.txt', 'r') as f:
    a = [int(x) for x in f]

    v = []
    for i in range(2, len(a) - 1):
        if abs(a[i]) % 10 == 7 and abs(a[i+1]) % 10 == 7:
            v.append(abs(a[i] - a[i+1]))
print(len(v), min(v))