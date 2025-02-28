with open('17_17558.txt', 'r') as f:
    a = [int(x) for x in f]
    z = len([x for x in a if x % 32 == 0])

    b = []
    for i in range(0, len(a) - 1):
        z1 = len([x for x in a[i:i+2] if x < 0])
        if sum(a[i:i+2]) < z and z1 >= 1:
            b.append(sum(a[i:i+2]))
print(len(b), max(b))

print(-137% 10)