import itertools

b = itertools.product('QRS', repeat=2)
b = [''.join(x) for x in b]
print(b)

with open('24_7600.txt', 'r') as f:
    a = f.readline()
    for i in b:
        a = a.replace(i, i[0] + ' ' + i[1])
    for i in b:
        a = a.replace(i, i[0] + ' ' + i[1])
    z = max([len(x) for x in a.split(' ')])
    print(z)
    print(a[:150])