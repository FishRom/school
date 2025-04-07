with open('17var03.txt', 'r') as f:
    a = [int(x) for x in f]
    mini = min(a)
    print(mini)
    b = []
    for i in range(len(a) - 1):
        if (a[i] % 44 + a[i+1] % 44) == mini:
            b.append(abs(a[i] - a[i+1]))
print(len(b), min(b))