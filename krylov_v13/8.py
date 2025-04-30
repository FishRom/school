import itertools

a = list(itertools.product('АТОМ', repeat=4))
a = [''.join(x) for x in a]
a.sort()
a = [x for x in a]
b = [x for x in a if x[0] == 'О']
print(a.index('ОААА') + 1)