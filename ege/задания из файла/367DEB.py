import itertools

a = list(itertools.product('АЛГОРИТМ', repeat=5))
a = [''.join(x) for x in a]
a.sort()
b = 0
m = 0
for x in a:
    m += 1
    if m % 2 == 0 and x[0] != 'Л' and x.count('И') >= 2:
        b += 1
print(b)