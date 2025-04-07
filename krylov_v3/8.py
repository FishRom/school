import itertools

a = list(itertools.product('123456', repeat=4))
a = [''.join(x) for x in a]
res = 0
b = []
for i in a:
    if i.count('3') == 1:
        z = i
        for j in range(3, 7):
            if j %2 == 0:
                z = z.replace(str(j), '2')
            else:
                z = z.replace(str(j), '1')
        if z.count('2') <= 2:
            res += 1

print(res)
