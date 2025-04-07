with open('17var02.txt', 'r') as f:
    a = [int(x) for x in f]
    mex = min([x for x in a])

    s = []
    for i in range(0, len(a) - 1):
        if len([x for x in a[i:i+2] if x % 30 == mex]):
            s.append(sum(a[i:i+2]))
print(len(s), min(s))