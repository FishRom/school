with open('17var20.txt', 'r') as f:
    a = [int(x) for x in f]
    #m = min([x for x in a if ])

    v = []
    for i in range(0, len(a) - 1):
        #a[i] * a[i+1] % 2 == 1
        if (abs(a[i]) % 10) != (abs(a[i+1]) % 10) and (a[i] * a[i+1]) % 2 == 1:
            v.append(abs(a[i]) * abs(a[i+1]))
print(len(v), min(v))