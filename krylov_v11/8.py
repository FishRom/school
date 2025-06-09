import itertools

a = list(itertools.product('СОРНЯК', repeat=6))
a = [''.join(x) for x in a]
a.sort()
b = [x for x in a if x.count('К') <= 3 and x.count('Я') == 2]
print([a.index(x) + 1 for x in b[:10]])