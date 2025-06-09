import itertools

a = list(itertools.product('МУЖЧИНА', repeat=6))
a = [''.join(x) for x in a]
a.sort()
m = 0
b = 0
for x in a:
    a = ''.join(x)
    m += 1
    if x[0] != 'Ж' and x.count('Ч') <= 1 and m % 2 == 0:
        b += 1
print(b)