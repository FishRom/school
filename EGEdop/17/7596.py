with (open('17_7596.txt', 'r') as f):
    a = [int(x) for x in f]
    z = min([x for x in a if x % 10 == 5 and x > 99])
    print(z)

    b = []
    for i in range(0, len(a) - 1):
        if len([x for x in a[i:i+2] if len(str(abs(x))) == 3]) == 1 and sum(a[i:i+2]) % z == 0:

            #len([x for x in a[i:i+2] if abs(x) % 10 == 5 and len(str(abs(x))) == 3] and sum(a[i:i+2]) % int(z) == 0):
            b.append(sum(a[i:i+2]))
print(len(b), min(b))